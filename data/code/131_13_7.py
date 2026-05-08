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
        final_message = f"Status: {status}, Score: {score}%, Result: {result}"
    elif status == "Fail":
        final_message = f"Status: {status}, Score: {score}%, Result: {result}. Action required."
    else:
        final_message = f"Status: {status}, Score: {score}%, Result: {result}. Status unknown."
    return final_message
if __name__ == '__main__':
    sample_score_1 = 95
    sample_status_1 = "Pass"
    sample_score_2 = 45
    sample_status_2 = "Fail"
    sample_score_3 = 82
    sample_status_3 = "Unknown"
    test_cases = [
        (sample_score_1, sample_status_1),
        (sample_score_2, sample_status_2),
        (sample_score_3, sample_status_3)
    ]
    for score, status in test_cases:
        try:
            output = decision_simulator(score, status)
            print(output)
        except Exception as e:
            print(f"An error occurred during simulation: {e}", file=sys.stderr)
    invalid_score = 105
    invalid_status = "Pass"
    try:
        print("\nTesting invalid input scenario:")
        output = decision_simulator(invalid_score, invalid_status)
        print(output)
    except Exception as e:
        print(f"An error occurred during invalid input test: {e}", file=sys.stderr)