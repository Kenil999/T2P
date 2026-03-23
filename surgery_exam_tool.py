#!/usr/bin/env python3
"""
Surgery Long-Answer Tool
------------------------
A focused CLI utility for final-year MBBS surgery theory preparation.

Features:
- Topic finder across a broad exam-oriented syllabus map.
- Long-answer writer for high-yield topics (exam-ready structure).
- Universal answer constructor for any topic using surgical long-answer framework.
- 2-day crisis mode: gives immediate, high-impact writing checklist (not a timetable).

Usage examples:
  python surgery_exam_tool.py list --category THYROID
  python surgery_exam_tool.py find --query "graves"
  python surgery_exam_tool.py answer --topic "Graves disease"
  python surgery_exam_tool.py answer --topic "Varicose veins" --depth concise
  python surgery_exam_tool.py framework --topic "Necrotizing fasciitis"
  python surgery_exam_tool.py rescue
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class TopicAnswer:
    title: str
    content: str
    keywords: Tuple[str, ...]


SYLLABUS: Dict[str, List[str]] = {
    "THYROID": [
        "Synthesis of thyroid hormones",
        "Causes of goiter",
        "Causes of hypothyroidism",
        "Hyperthyroidism",
        "Graves disease: clinical features, diagnosis and management",
        "Thyroglossal cyst and fistula",
        "Sistrunk operation",
        "Clinical approach to thyroid swelling",
        "Classification and diagnosis of solitary thyroid nodule",
        "Multinodular goiter",
        "Thyroid malignancy",
        "Papillary carcinoma thyroid",
        "Hurthle cell tumor",
        "Medullary thyroid carcinoma",
        "Anaplastic thyroid carcinoma",
        "Complications of thyroidectomy",
    ],
    "BREAST": [
        "Lymphatic drainage of breast",
        "ANDI classification",
        "Tubercular mastitis",
        "Phyllodes tumor",
        "Approach to breast lump",
        "Triple assessment",
        "Risk factors for breast cancer",
        "Carcinoma breast: pathology, staging and management",
        "Cutaneous manifestations of breast cancer",
        "Management of early breast carcinoma",
        "Locally advanced breast cancer (T4)",
        "Male breast cancer",
        "BIRADS V TNBC management",
    ],
    "SHOCK_AND_RESUSCITATION": [
        "SIRS",
        "Definition and classification of shock",
        "Hemorrhagic shock: etiology and management",
        "Septic shock",
        "Monitoring in shock",
        "Plasma substitutes",
        "Indications of blood transfusion",
        "Massive blood transfusion",
        "Complications of blood transfusion",
    ],
    "TRAUMA": [
        "Primary survey ABCDE",
        "Secondary survey",
        "FAST and E-FAST",
        "Damage control resuscitation",
        "Damage control surgery",
        "Blunt abdominal trauma",
        "Tension pneumothorax",
        "Flail chest",
        "Cardiac tamponade vs tension pneumothorax",
    ],
    "SKIN_SOFT_TISSUE": [
        "Definition and classification of ulcer",
        "Lipoma",
        "Keloid vs hypertrophic scar",
        "Dry vs wet gangrene",
        "Rodent ulcer",
        "Basal cell carcinoma",
        "Squamous cell carcinoma",
        "Marjolin ulcer",
        "Malignant melanoma",
    ],
    "NUTRITION_WOUND_INFECTION": [
        "Enteral vs parenteral nutrition",
        "Total parenteral nutrition",
        "Phases of wound healing",
        "Classification of surgical wounds",
        "Management of acute wound",
        "Necrotizing fasciitis",
        "Hilton's method of abscess drainage",
    ],
    "VASCULAR": [
        "Critical limb ischemia",
        "Buerger disease",
        "Raynaud phenomenon",
        "Varicose veins",
        "Venous ulcer",
        "DVT prophylaxis and treatment",
        "Pulmonary embolism",
    ],
    "OTHER_HIGH_YIELD": [
        "Glasgow coma scale",
        "Subdural hematoma",
        "Burns: assessment and fluid management",
        "Leukoplakia",
        "Oral submucous fibrosis",
        "Pleomorphic adenoma parotid",
        "Universal precautions",
        "Acute hyperkalemia management",
        "Empyema necessitans",
    ],
}


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


ANSWERS: List[TopicAnswer] = [
    TopicAnswer(
        title="Graves disease: clinical features, diagnosis and management",
        keywords=("graves", "hyperthyroidism", "thyrotoxicosis", "diffuse toxic goiter"),
        content=textwrap.dedent(
            """
            Definition:
            Graves disease is an autoimmune disorder causing thyrotoxicosis due to thyroid-stimulating immunoglobulins (TSI) activating TSH receptors, usually with diffuse toxic goiter and extra-thyroid manifestations.

            Etiopathogenesis:
            1) Autoantibodies: TSH receptor antibodies stimulate follicular cells.
            2) Genetic predisposition: HLA associations, family clustering.
            3) Triggers: stress, infection, smoking, postpartum immune rebound.
            4) Extra-thyroid tissue involvement: fibroblast activation in orbit and pretibial skin.

            Clinical features:
            A. Hypermetabolic symptoms:
               - Weight loss despite increased appetite
               - Heat intolerance, sweating
               - Palpitations, tremors, anxiety, irritability
               - Proximal muscle weakness, fatigability
               - Increased bowel frequency
            B. Thyroid findings:
               - Diffuse soft vascular goiter, bruit may be present
            C. Eye signs:
               - Staring look, lid lag/retraction
               - Exophthalmos, periorbital edema, ophthalmoplegia (in severe disease)
            D. Skin and systemic:
               - Warm moist skin, fine hair
               - Pretibial myxedema (uncommon but specific)
               - Atrial fibrillation in severe/elderly patients

            Diagnosis:
            1) Thyroid function tests:
               - Low TSH (suppressed)
               - Elevated free T4 and/or free T3
            2) Autoimmunity:
               - TSH receptor antibody positive supports Graves.
            3) Imaging:
               - Thyroid ultrasound with diffuse increased vascularity.
               - Radioisotope uptake: diffuse increased uptake (if needed).
            4) Baseline before therapy:
               - CBC, liver function tests, ECG, eye assessment.

            Management:
            I. Symptomatic control:
               - Beta blockers (e.g., propranolol) for tachycardia/tremor.

            II. Definitive control of hyperthyroidism:
               A) Antithyroid drugs (first line in many young patients)
                  - Methimazole/carbimazole preferred (except early pregnancy).
                  - PTU preferred in first trimester or thyroid storm.
                  - Monitor TFT regularly; usual duration 12–18 months.
               B) Radioiodine ablation
                  - Effective definitive option, avoid in pregnancy/lactation.
                  - Caution in active severe ophthalmopathy.
               C) Surgery (near-total/total thyroidectomy)
                  Indications:
                  - Large goiter/compressive symptoms
                  - Suspicious nodule/cancer concern
                  - Drug intolerance or relapse
                  - Preference for rapid definitive control
                  Pre-op preparation:
                  - Render euthyroid, beta-blockade, iodine in selected cases.

            III. Ophthalmopathy management:
               - Stop smoking, lubricants, selenium (selected mild cases), steroids for active moderate-severe disease, orbital decompression if vision threat.

            Complications to mention in exam:
            - Thyroid storm, AF, heart failure, osteoporosis, ophthalmic optic neuropathy.

            Exam conclusion:
            Graves disease is a systemic autoimmune disease; treatment is individualized by age, goiter size, fertility plans, eye involvement, and patient preference.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Solitary thyroid nodule: diagnostic approach and management",
        keywords=("solitary thyroid nodule", "stn", "thyroid nodule"),
        content=textwrap.dedent(
            """
            Definition:
            Solitary thyroid nodule (STN) is a discrete palpable or radiologically distinct lesion in an otherwise normal thyroid gland.

            Importance:
            Main objective is to rule out malignancy while avoiding unnecessary surgery.

            Etiology:
            - Benign colloid nodule
            - Follicular adenoma
            - Thyroid cyst/hemorrhagic cyst
            - Dominant nodule in multinodular goiter
            - Thyroiditis-related nodule
            - Malignancy: papillary, follicular, medullary, anaplastic, lymphoma, metastasis

            Clinical evaluation:
            1) History:
               - Rapid growth, pressure symptoms, voice change, radiation exposure, family history (medullary/MEN2), hyper/hypothyroid symptoms.
            2) Examination:
               - Nodule size, consistency, mobility, cervical nodes, vocal cord function (indirectly via voice), signs of thyrotoxicosis.

            Investigations (Triple approach in thyroid):
            1) TSH first-line test.
            2) Ultrasound neck + TIRADS risk stratification.
            3) US-guided FNAC (Bethesda reporting) for suspicious or size-eligible nodules.
            4) If TSH suppressed: radionuclide scan to identify hot vs cold nodule.
            5) Calcitonin if medullary suspicion/family history.
            6) Laryngoscopy pre-op when voice change/previous surgery.

            Red flag ultrasound features:
            - Hypoechoic solid nodule, microcalcification, irregular margin, taller-than-wide shape, extrathyroidal extension, suspicious nodes.

            Management:
            A) Benign cytology:
               - Observation with periodic US.
               - Surgery if large symptomatic/cosmetic concern.
            B) Indeterminate cytology (Bethesda III/IV):
               - Repeat FNAC, molecular test (where available), diagnostic hemithyroidectomy.
            C) Suspicious/malignant cytology:
               - Oncologic surgery as per type/risk (hemi vs total thyroidectomy ± node dissection).
            D) Toxic autonomous nodule:
               - Radioiodine or surgery after control.
            E) Cystic nodule:
               - Aspiration; recurrent/suspicious cyst may need surgery.

            Surgical principles:
            - Hemithyroidectomy for selected low-risk unilateral disease.
            - Total thyroidectomy for bilateral disease, high-risk cancer, or specific histologies.

            Follow-up:
            - Histopathology-guided further treatment, thyroid hormone replacement when indicated, long-term surveillance.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Complications of thyroidectomy",
        keywords=("complications of thyroidectomy", "thyroidectomy complications", "hypocalcemia"),
        content=textwrap.dedent(
            """
            Complications are best described as immediate, early, and late.

            Immediate / early:
            1) Reactionary hemorrhage and neck hematoma:
               - Can cause airway obstruction; surgical emergency.
            2) Respiratory compromise:
               - Due to hematoma, laryngeal edema, tracheomalacia (rare).
            3) Recurrent laryngeal nerve (RLN) injury:
               - Unilateral: hoarseness; bilateral: stridor/airway obstruction.
            4) External branch of superior laryngeal nerve injury:
               - Voice fatigue, inability to produce high-pitched sounds.
            5) Hypocalcemia / hypoparathyroidism:
               - Perioral numbness, tetany, carpopedal spasm; Chvostek/Trousseau signs.
            6) Thyroid storm (rare, usually inadequately prepared toxic patient).

            Late:
            1) Permanent hypoparathyroidism.
            2) Permanent RLN palsy.
            3) Hypothyroidism (expected after total thyroidectomy).
            4) Scar issues (hypertrophic/keloid), recurrence in subtotal procedures.

            Prevention:
            - Meticulous hemostasis, nerve identification/preservation, careful parathyroid preservation with autotransplant when needed, appropriate pre-op euthyroid preparation.

            Management outline:
            - Expanding neck swelling: open wound immediately and shift to OT.
            - Symptomatic hypocalcemia: IV calcium then oral calcium + vitamin D.
            - Vocal cord palsy: laryngoscopy confirmation, voice therapy ± medialization.
            - Hypothyroidism: levothyroxine replacement.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Approach to a breast lump and triple assessment",
        keywords=("breast lump", "triple assessment", "breast lesion"),
        content=textwrap.dedent(
            """
            Principle:
            Every breast lump is malignant until proven otherwise, but evaluated systematically to avoid over-treatment.

            Triple assessment (gold standard):
            1) Clinical assessment
            2) Imaging
            3) Pathology
            Concordance among all 3 gives highest diagnostic accuracy.

            1) Clinical assessment:
            - History: age, duration, pain, cyclicity, nipple discharge, family history, reproductive history, hormonal exposure, constitutional symptoms.
            - Examination: inspect both breasts and axillae; note site, size, consistency, mobility, skin changes, nipple retraction, peau d'orange, nodes.

            2) Imaging:
            - <35 years: ultrasound first.
            - ≥35 years: bilateral mammography ± tomosynthesis plus targeted ultrasound.
            - MRI in selected high-risk, occult primary, dense breasts, implant evaluation.
            - BIRADS grading guides further steps.

            3) Pathology:
            - FNAC for quick cytology where suitable.
            - Core needle biopsy preferred for definitive histology and receptor status (ER/PR/HER2, Ki-67).

            Management by common scenarios:
            - Simple cyst: aspiration if symptomatic; reassess if recurrent/bloody.
            - Fibroadenoma: observe if classic stable small lesion; excise if large/growing/symptomatic.
            - Suspicious/malignant lesion: stage, molecular subtype, MDT treatment.

            Red flags for malignancy:
            - Hard irregular fixed lump, skin tethering/ulceration, nipple retraction, bloody discharge, hard axillary nodes.

            Exam ending line:
            Triple assessment with radiology-pathology-clinical concordance is mandatory before definitive surgery.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Carcinoma breast: staging and management",
        keywords=("carcinoma breast", "breast cancer", "tnm", "t4"),
        content=textwrap.dedent(
            """
            Overview:
            Breast cancer management is stage-based and biology-based (ER/PR/HER2, grade, Ki-67, genomic risk when available).

            Risk factors:
            - Female sex, increasing age
            - Family history/BRCA mutation
            - Early menarche, late menopause, nulliparity, late first childbirth
            - Hormonal exposure, obesity (postmenopausal), alcohol, prior chest irradiation

            Clinical features:
            - Painless hard irregular lump
            - Nipple retraction/discharge
            - Skin dimpling/peau d'orange/ulceration
            - Axillary node involvement

            TNM essentials (exam gist):
            - T1/T2: smaller localized tumors
            - T3: >5 cm
            - T4: chest wall/skin involvement including inflammatory carcinoma
            - N stage based on nodal burden/fixity/internal mammary/supraclavicular
            - M1 indicates distant metastasis

            Work-up:
            1) Triple assessment and core biopsy.
            2) Receptor profile: ER/PR/HER2.
            3) Baseline staging (for stage III/IV or symptomatic): CT/PET-CT as indicated, bone scan selectively.
            4) Routine pre-treatment fitness tests.

            Management:
            A) Early breast cancer (stage I–II):
               - Breast-conserving surgery + sentinel node biopsy, followed by radiotherapy (when feasible),
                 OR modified radical mastectomy depending on tumor-breast ratio and preference.
               - Adjuvant systemic therapy based on receptor/molecular risk.
            B) Locally advanced (stage III / T4):
               - Usually neoadjuvant chemotherapy first.
               - Reassess response, then surgery (often MRM) ± axillary dissection.
               - Post-op radiotherapy and adjuvant endocrine/targeted therapy.
            C) Metastatic disease:
               - Systemic palliative intent therapy, local measures for symptom control.

            Subtype-directed adjuvant therapy:
            - HR+ : endocrine therapy (tamoxifen/aromatase inhibitor).
            - HER2+ : anti-HER2 therapy with chemotherapy.
            - TNBC: chemotherapy backbone ± immunotherapy in selected settings.

            Follow-up:
            - Clinical exam, treatment toxicity monitoring, annual imaging of remaining breast tissue, survivorship counseling.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Define and classify shock",
        keywords=("shock", "classify shock", "types of shock"),
        content=textwrap.dedent(
            """
            Definition:
            Shock is a life-threatening state of acute circulatory failure leading to inadequate tissue perfusion, cellular hypoxia, and organ dysfunction.

            Classification:
            1) Hypovolemic shock
               - Hemorrhagic (trauma, GI bleed, obstetric bleed)
               - Non-hemorrhagic (dehydration, burns, third-space loss)
            2) Cardiogenic shock
               - MI, severe cardiomyopathy, arrhythmia, valvular/mechanical causes
            3) Obstructive shock
               - Tension pneumothorax, cardiac tamponade, massive pulmonary embolism
            4) Distributive shock
               - Septic, anaphylactic, neurogenic

            Pathophysiological stages:
            - Compensated: tachycardia, vasoconstriction maintains BP.
            - Decompensated: hypotension, tissue hypoperfusion.
            - Irreversible: refractory cellular failure, multiorgan dysfunction.

            Clinical features:
            - Tachycardia, hypotension, altered sensorium, cold clammy skin (except early distributive), oliguria, raised lactate.

            Basic management principles:
            1) Early recognition and call for help.
            2) ABC resuscitation, oxygen, airway support.
            3) Two large-bore IV lines, blood sampling, lactate.
            4) Targeted fluid therapy and blood products when needed.
            5) Treat cause urgently (bleeding control, antibiotics, decompression, reperfusion, epinephrine etc.).
            6) Continuous monitoring and endpoint-guided resuscitation (MAP, urine output, lactate clearance).
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Hemorrhagic shock: etiology, features and management",
        keywords=("hemorrhagic shock", "hypovolemic shock", "blood loss"),
        content=textwrap.dedent(
            """
            Definition:
            Hemorrhagic shock is hypovolemic shock caused by acute blood loss resulting in inadequate tissue oxygen delivery.

            Etiology:
            - Trauma (external/internal bleeding)
            - GI hemorrhage
            - Obstetric/gynecologic bleeding
            - Perioperative/postoperative hemorrhage
            - Ruptured aneurysm

            Clinical features:
            - Tachycardia, narrow pulse pressure, hypotension (late), cool clammy skin, delayed capillary refill, tachypnea, oliguria, altered mentation.

            ATLS-oriented management:
            1) Primary survey and hemorrhage control:
               - Airway with cervical spine protection
               - High-flow oxygen/ventilation support
               - External bleed control: direct pressure, tourniquet, pelvic binder as indicated
            2) Vascular access and labs:
               - Two large-bore IV or IO access; CBC, coagulation, ABG/lactate, crossmatch.
            3) Damage control resuscitation:
               - Permissive hypotension (except TBI/pregnancy specific caution)
               - Balanced transfusion (PRBC:FFP:platelets approximately 1:1:1 in massive bleed protocols)
               - Early tranexamic acid in trauma windows
               - Avoid excessive crystalloids
            4) Definitive hemorrhage control:
               - Surgery, endoscopy, angioembolization, obstetric intervention depending source.
            5) Monitoring endpoints:
               - MAP, urine output (>0.5 mL/kg/h adults), mental status, lactate clearance, base deficit.
            6) Prevent triad of death:
               - Hypothermia, acidosis, coagulopathy correction.

            Complications:
            - AKI, ARDS, DIC, MOF, transfusion-related complications.

            Exam conclusion:
            Survival depends on simultaneous resuscitation and definitive source control—not sequential delay.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Primary survey of trauma patient (ABCDE)",
        keywords=("abcde", "primary survey", "trauma", "rta"),
        content=textwrap.dedent(
            """
            Definition:
            Primary survey is rapid, structured identification and treatment of immediately life-threatening injuries in trauma.

            A – Airway with cervical spine protection:
            - Assess patency, speech, obstruction signs.
            - Jaw thrust, suction, adjuncts, definitive airway if needed.
            - Maintain C-spine immobilization.

            B – Breathing and ventilation:
            - Inspect, palpate, percuss, auscultate chest.
            - Identify/treat life threats: tension pneumothorax, open pneumothorax, massive hemothorax, flail chest.
            - Oxygen and ventilatory support.

            C – Circulation with hemorrhage control:
            - Check pulse, BP, skin perfusion.
            - Control external bleeding, obtain IV/IO access, initiate fluid/blood resuscitation.
            - Consider FAST/E-FAST for internal bleeding.

            D – Disability (neurologic status):
            - GCS, pupils, limb movement, capillary glucose.

            E – Exposure and environment:
            - Fully expose to detect injuries, then prevent hypothermia (warm blankets, warmed fluids).

            Adjuncts during primary survey:
            - Monitoring: ECG, pulse oximetry, BP, urine output.
            - ABG/lactate, portable X-rays, FAST/E-FAST.

            Reassessment:
            - Repeat ABCDE after every intervention; deterioration mandates restart from A.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="FAST and E-FAST in trauma",
        keywords=("fast", "e-fast", "ultrasound trauma"),
        content=textwrap.dedent(
            """
            FAST (Focused Assessment with Sonography in Trauma):
            Bedside ultrasound to detect free fluid in peritoneal, pericardial spaces in unstable trauma.

            Standard FAST windows:
            1) Right upper quadrant (hepatorenal/Morrison pouch)
            2) Left upper quadrant (splenorenal recess)
            3) Pelvis (pouch of Douglas/rectovesical)
            4) Subxiphoid/pericardial view

            E-FAST extends FAST by adding thoracic views:
            - Pleural sliding for pneumothorax
            - Pleural fluid for hemothorax

            Advantages:
            - Rapid, repeatable, bedside, no radiation, useful in unstable patients.

            Limitations:
            - Operator dependent
            - May miss hollow viscus injury/retroperitoneal injury/small fluid collections.

            Clinical integration:
            - Unstable + positive FAST -> urgent operative/interventional source control.
            - Stable + positive/indeterminate FAST -> further CT-based evaluation.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Varicose veins: clinical features and management",
        keywords=("varicose", "venous ulcer", "venous insufficiency"),
        content=textwrap.dedent(
            """
            Definition:
            Varicose veins are dilated, elongated, tortuous superficial veins due to valvular incompetence and venous hypertension, commonly in lower limbs.

            Etiology/risk factors:
            - Primary valvular failure
            - Secondary causes: DVT/post-thrombotic syndrome
            - Prolonged standing, obesity, pregnancy, family history

            Clinical features:
            - Visible dilated veins, aching/heaviness, evening edema, cramps, itching.
            - Skin changes in chronic venous disease: hyperpigmentation, eczema, lipodermatosclerosis, venous ulcer (gaiter area).

            Evaluation:
            - Clinical CEAP classification.
            - Duplex venous ultrasound (gold standard) to map reflux and obstruction.

            Management:
            1) Conservative:
               - Leg elevation, exercise, weight control, compression stockings, skin care.
            2) Interventions:
               - Endovenous thermal ablation (laser/radiofrequency) preferred in many cases.
               - Ultrasound-guided foam sclerotherapy.
               - Surgical ligation/stripping or phlebectomy in selected patterns.
            3) Ulcer care:
               - Compression therapy is cornerstone + wound care + treat reflux source.

            Complications:
            - Bleeding from varix, superficial thrombophlebitis, venous ulcer recurrence.
            """
        ).strip(),
    ),
    TopicAnswer(
        title="Burns: assessment and fluid management",
        keywords=("burn", "fluid management burn", "third degree burn"),
        content=textwrap.dedent(
            """
            Burn classification:
            1) By depth: superficial, superficial partial thickness, deep partial thickness, full thickness.
            2) By extent: % TBSA using Rule of 9s (adult) or Lund-Browder chart (children).

            Initial management principles:
            - Stop burning process, airway and breathing assessment, oxygen.
            - Early recognition of inhalational injury.
            - IV access through unburned skin if possible.

            Fluid resuscitation:
            - Common formula: 4 mL x body weight (kg) x %TBSA (Ringer lactate) in first 24 h.
            - Give 50% in first 8 h from time of burn, remaining over next 16 h.
            - Titrate to endpoints: urine output (adults ~0.5 mL/kg/h), perfusion, lactate.

            Wound care:
            - Cleanse, debride loose tissue, topical antimicrobials, dressings.
            - Tetanus prophylaxis, analgesia, nutrition support.

            Full-thickness/major burns:
            - Early excision and grafting where feasible.
            - Monitor for compartment syndrome, sepsis, AKI.

            Electrical burns:
            - Suspect deep tissue injury, arrhythmia, myoglobinuria.
            - Aggressive fluids and cardiac monitoring as indicated.
            """
        ).strip(),
    ),
]


def all_topics() -> List[str]:
    items: List[str] = []
    for cat, topics in SYLLABUS.items():
        for t in topics:
            items.append(f"{cat}: {t}")
    return items


def find_topics(query: str) -> List[str]:
    q = _clean(query)
    scored: List[Tuple[int, str]] = []
    for item in all_topics():
        text = _clean(item)
        score = 0
        if q in text:
            score += 5
        for token in q.split():
            if token in text:
                score += 1
        if score > 0:
            scored.append((score, item))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [s[1] for s in scored[:25]]


def get_answer(topic: str) -> TopicAnswer | None:
    q = _clean(topic)
    best: Tuple[int, TopicAnswer] | None = None
    for ans in ANSWERS:
        score = 0
        if q in _clean(ans.title):
            score += 5
        for k in ans.keywords:
            ck = _clean(k)
            if q == ck:
                score += 6
            elif q in ck or ck in q:
                score += 3
            for token in q.split():
                if token and token in ck:
                    score += 1
        for token in q.split():
            if token in _clean(ans.title):
                score += 1
        if score > 0 and (best is None or score > best[0]):
            best = (score, ans)
    return best[1] if best else None


def generic_framework(topic: str, depth: str = "full") -> str:
    intro = (
        f"{topic}: exam-ready long answer template\n"
        "Use this exact order in the exam to maximize marks and presentation quality."
    )
    blocks = [
        "1) Definition (1-2 lines: precise, standard, disease-specific)",
        "2) Etiology / Risk factors (classify under major headings)",
        "3) Etiopathogenesis / Pathophysiology (stepwise mechanism)",
        "4) Classification (accepted system: clinical/radiological/pathological/staging)",
        "5) Clinical features (symptoms -> signs -> complications)",
        "6) Investigations (baseline, confirmatory, staging/severity, differential)",
        "7) Management (resuscitation/medical/surgical/definitive, with indications)",
        "8) Complications (disease + treatment-related)",
        "9) Prognosis and follow-up",
        "10) One-line exam conclusion (holistic, stage-based, patient-centered)",
    ]
    high_yield = [
        "Always write one flowchart: 'Patient presents with X -> first test -> confirmatory test -> definitive management'.",
        "Underline key terms: indications, contraindications, gold standard, complications.",
        "If oncology topic: include TNM/stage + receptor/molecular profile + MDT approach.",
        "If emergency topic: start with ABCDE and simultaneous cause control.",
        "If procedure asked: include pre-op, key steps, post-op care, and complications.",
    ]

    if depth == "concise":
        blocks = blocks[:7]
        high_yield = high_yield[:3]

    lines = [intro, "", "Suggested structure:"]
    lines.extend([f"- {b}" for b in blocks])
    lines.append("")
    lines.append("High-yield writing rules:")
    lines.extend([f"- {h}" for h in high_yield])
    lines.append("")
    lines.append(
        "Emergency close for most answers: 'Early diagnosis, protocol-based resuscitation, and timely definitive intervention improve survival and reduce morbidity.'"
    )
    return "\n".join(lines)


def rescue_mode() -> str:
    return textwrap.dedent(
        """
        2-Day Surgery Theory Rescue Tool (No timetable, only output-maximizing method)

        A) What to do for every long answer (universal scoring engine):
        1. Start with Definition (2 lines)
        2. Write Classification (even if short)
        3. Write Clinical features in 3 headings: Symptoms, Signs, Complications
        4. Write Investigations as: baseline -> confirmatory -> staging/severity
        5. Write Management as: initial stabilization -> definitive treatment -> follow-up
        6. End with 1-line conclusion

        B) Mandatory high-yield buckets (most repeated + scoring):
        - Thyroid: Graves, STN, MNG, thyroidectomy complications.
        - Breast: Triple assessment, carcinoma staging + management, early vs locally advanced.
        - Shock/Trauma: shock classification, hemorrhagic shock management, ABCDE, FAST/E-FAST.
        - Vascular: varicose veins + DVT/PE basics.
        - Burns and wounds: burn fluid formula, wound healing, necrotizing fasciitis.

        C) Examiner-pleasing style:
        - Use headings and subheadings, no large paragraph blocks.
        - Add one mini algorithm in arrows.
        - Add one table when possible (e.g., dry vs wet gangrene, tamponade vs tension pneumothorax).
        - Mention one guideline-style principle (e.g., ABCDE, triple assessment, MDT approach).

        D) When you blank out in exam:
        Write this skeleton and fill what you remember:
        Definition -> causes -> pathogenesis -> features -> investigations -> treatment -> complications -> prognosis.

        E) Golden emergency lines (safe marks):
        - "Resuscitation and definitive source control must proceed simultaneously."
        - "Management is stage-based and multidisciplinary."
        - "Close monitoring of vitals, urine output, and complications is essential."
        """
    ).strip()


def format_text_block(text: str, width: int = 100) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped.startswith(("-", "*", "1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)", "10)", "A)", "B)", "C)", "D)", "E)", "I.", "II.", "III.", "IV.", "V.")):
            lines.append(stripped)
            continue
        wrapped = textwrap.fill(stripped, width=width)
        lines.append(wrapped)
    return "\n".join(lines)


def list_topics(category: str | None) -> str:
    if category is None:
        output = ["Available categories:"]
        for cat in SYLLABUS:
            output.append(f"- {cat} ({len(SYLLABUS[cat])} topics)")
        output.append("\nUse --category to view topics in one category.")
        return "\n".join(output)

    cat_up = category.strip().upper()
    if cat_up not in SYLLABUS:
        candidates = [c for c in SYLLABUS if cat_up in c]
        if not candidates:
            return f"Category '{category}' not found. Run `list` without --category."
        cat_up = candidates[0]

    output = [f"{cat_up} topics:"]
    for i, topic in enumerate(SYLLABUS[cat_up], start=1):
        output.append(f"{i}. {topic}")
    return "\n".join(output)


def run_cli(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="surgery_exam_tool",
        description="Long-answer focused MBBS surgery exam helper.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List syllabus categories or topics in a category")
    p_list.add_argument("--category", type=str, default=None)

    p_find = sub.add_parser("find", help="Search topics")
    p_find.add_argument("--query", required=True, type=str)

    p_answer = sub.add_parser("answer", help="Generate long answer for a known high-yield topic")
    p_answer.add_argument("--topic", required=True, type=str)
    p_answer.add_argument("--depth", choices=["full", "concise"], default="full")

    p_framework = sub.add_parser("framework", help="Get universal long-answer framework for any topic")
    p_framework.add_argument("--topic", required=True, type=str)
    p_framework.add_argument("--depth", choices=["full", "concise"], default="full")

    sub.add_parser("rescue", help="Get 2-day no-timetable high-yield writing method")

    args = parser.parse_args(argv)

    if args.command == "list":
        print(list_topics(args.category))
        return 0

    if args.command == "find":
        results = find_topics(args.query)
        if not results:
            print("No matching topics found.")
            return 1
        print("Top matching topics:")
        for idx, item in enumerate(results, start=1):
            print(f"{idx}. {item}")
        return 0

    if args.command == "answer":
        answer = get_answer(args.topic)
        if answer is None:
            print("No exact high-yield answer found for this topic.")
            print("Use framework mode:")
            print(generic_framework(args.topic, depth=args.depth))
            return 1
        out = answer.content
        if args.depth == "concise":
            paragraphs = [p.strip() for p in out.split("\n\n") if p.strip()]
            out = "\n\n".join(paragraphs[:6])
        print(f"Topic: {answer.title}\n")
        print(format_text_block(out))
        return 0

    if args.command == "framework":
        print(format_text_block(generic_framework(args.topic, depth=args.depth)))
        return 0

    if args.command == "rescue":
        print(format_text_block(rescue_mode()))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(run_cli(sys.argv[1:]))
