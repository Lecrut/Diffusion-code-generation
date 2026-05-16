import sys
def decision_simulator(score, attempt):
    if score >= 90:
        return "Grade A: Excellent performance."
    elif score >= 80:
        return "Grade B: Good performance."
    elif score >= 70:
        return "Grade C: Satisfactory performance."
    elif score >= 60:
        return "Grade D: Needs improvement."
    elif score >= 50:
        return "Grade F: Poor performance."
    else:
        return "Invalid score. Score must be between 0 and 100."
def process_decision(input_value):
    try:
        score = int(input_value)
        if not (0 <= score <= 100):
            raise ValueError("Score out of range.")
        if score < 0 or score > 100:
            return decision_simulator(score, 1)
        else:
            return decision_simulator(score, 1)
    except ValueError as e:
        return f"Error: Invalid input provided. Details: {e}"
    except TypeError:
        return "Error: Input must be a numerical value."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_inputs = [
        "95",
        "72",
        "45",
        "105",
        "abc",
        "-10",
        "88"
    ]
    print("--- Decision Simulation Results ---")
    for input_val in sample_inputs:
        result = process_decision(input_val)
        print(f"Input: '{input_val}' -> Result: {result}")
        print("-" * 30)