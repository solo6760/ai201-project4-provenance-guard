import os
from app import calculate_linguistic_complexity, combine_signals_and_calibrate

TEST_INPUTS = {
    "Clearly AI-generated": (
        "Artificial intelligence represents a transformative paradigm shift in modern society. "
        "It is important to note that while the benefits of AI are numerous, it is equally "
        "essential to consider the ethical implications. Furthermore, stakeholders across "
        "various sectors must collaborate to ensure responsible deployment."
    ),
    "Clearly human-written": (
        "ok so i finally tried that new ramen place downtown and honestly? "
        "underwhelming. the broth was fine but they put WAY too much sodium in it and "
        "i was thirsty for like three hours after. my friend got the spicy version and "
        "said it was better. probably won't go back unless someone drags me there"
    ),
    "Borderline: formal human writing": (
        "The relationship between monetary policy and asset price inflation has been "
        "extensively studied in the literature. Central banks face a fundamental tension "
        "between their mandate for price stability and the unintended consequences of "
        "prolonged low interest rates on equity and real estate valuations."
    ),
    "Borderline: lightly edited AI output": (
        "I've been thinking a lot about remote work lately. There are genuine tradeoffs — "
        "flexibility and no commute on one side, isolation and blurred work-life boundaries "
        "on the other. Studies show productivity varies widely by individual and role type."
    )
}

def run_tests():
    print("=== Provenance Guard Scoring Calibration Test ===")
    for label, text in TEST_INPUTS.items():
        s2 = calculate_linguistic_complexity(text)
        # S1 (Groq) is simulated as None for local CLI test to test fallback logic
        p_ai_fallback, attr_fallback, conf_fallback = combine_signals_and_calibrate(None, s2)
        
        print(f"\nInput: {label}")
        print(f"  Text preview: \"{text[:75]}...\"")
        print(f"  Signal 2 (Local Heuristics): {s2:.4f}")
        print(f"  Combined (Fallback): Probability={p_ai_fallback:.4f}, Attribution={attr_fallback}, Confidence={conf_fallback:.4f}")

if __name__ == "__main__":
    run_tests()
