import sys
def decision_simulator(score, status):
    if score >= 90:
        result = "Excellent"
    elif score >= 70:
        result = "Good"
    elif score >= 50:
        result = "Average"
    elif score >= 30:
        result = "Needs Improvement"
    else:
        result = "Failing"
    if status == "Pass":
        final_message = f"Score: {score}%, Status: {status}. Result: {result}."
    elif status == "Fail":
        final_message = f"Score: {score}%, Status: {status}. Result: {result}. Action required."
    else:
        final_message = f"Invalid status provided: {status}."
    return final_message
if __name__ == '__main__':
    sample_score_1 = 95
    sample_status_1 = "Pass"
    sample_score_2 = 45
    sample_status_2 = "Fail"
    sample_score_3 = 82
    sample_status_3 = "Pass"
    sample_score_4 = 25
    sample_status_4 = "Pass"
    print(decision_simulator(sample_score_1, sample_status_1))
    print("-" * 30)
    print(decision_simulator(sample_score_2, sample_status_2))
    print("-" * 30)
    print(decision_simulator(sample_score_3, sample_status_3))
    print("-" * 30)
    print(decision_simulator(sample_score_4, sample_status_4))
    print("-" * 30)
    try:
        invalid_score = 100
        invalid_status = "Unknown"
        print(decision_simulator(invalid_score, invalid_status))
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)