import sys
def decision_simulator(score, effort):
    if score >= 90 and effort >= 8:
        result = "Excellent performance. High reward achieved."
    elif score >= 70 and effort >= 5:
        result = "Good performance. Moderate reward achieved."
    elif score >= 50 and effort >= 3:
        result = "Average performance. Low reward achieved."
    elif score >= 0 and effort < 3:
        result = "Poor performance. Minimal reward achieved."
    else:
        result = "Insufficient data or very low metrics."
    return result
if __name__ == '__main__':
    sample_score_1 = 95
    sample_effort_1 = 9
    sample_score_2 = 65
    sample_effort_2 = 4
    sample_score_3 = 40
    sample_effort_3 = 2
    sample_score_4 = 80
    sample_effort_4 = 6
    inputs = [
        (sample_score_1, sample_effort_1),
        (sample_score_2, sample_effort_2),
        (sample_score_3, sample_effort_3),
        (sample_score_4, sample_effort_4)
    ]
    for score, effort in inputs:
        try:
            output = decision_simulator(score, effort)
            print(f"Score: {score}, Effort: {effort} -> Decision: {output}")
        except Exception as e:
            print(f"An error occurred during simulation for input ({score}, {effort}): {e}", file=sys.stderr)
            print("Error handling activated.", file=sys.stderr)
            continue