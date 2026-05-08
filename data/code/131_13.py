import sys
def decision_simulator(score, status):
    if score >= 90:
        return "Excellent", "Pass"
    elif score >= 70:
        return "Good", "Pass"
    elif score >= 50:
        return "Average", "Review"
    elif score >= 30:
        return "Poor", "Fail"
    else:
        return "Failing", "Fail"
def process_input(input_score, input_status):
    try:
        score = int(input_score)
        status = input_status.lower()
    except ValueError:
        return "Error", "Invalid input for score."
    if not isinstance(score, int) or not isinstance(status, str):
        return "Error", "Invalid data types provided."
    if score < 0 or score > 100:
        return "Error", "Score must be between 0 and 100."
    if status == "pass" or status == "fail" or status == "review":
        result_type, action = decision_simulator(score, status)
        return result_type, action
    else:
        return "Error", "Invalid status provided. Must be 'Pass', 'Fail', or 'Review'."
if __name__ == '__main__':
    sample_inputs = [
        ("85", "Pass"),
        ("45", "Review"),
        ("92", "Pass"),
        ("25", "Fail"),
        ("105", "Pass"),
        ("abc", "Pass"),
        ("60", "Unknown"),
        ("-10", "Pass")
    ]
    print("--- Decision Simulation Results ---")
    for score_str, status_str in sample_inputs:
        print(f"\nInput Score: {score_str}, Input Status: {status_str}")
        result_type, action = process_input(score_str, status_str)
        print(f"Result Type: {result_type}, Action: {action}")
    print("\n--- Simulation Complete ---")