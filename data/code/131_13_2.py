import sys
def decision_simulator(score, effort):
    if score >= 90 and effort >= 8:
        result = "Excellent performance, high effort. Reward: Gold Medal."
    elif score >= 70 and effort >= 5:
        result = "Good performance, moderate effort. Reward: Silver Medal."
    elif score >= 50 and effort >= 3:
        result = "Satisfactory performance, low effort. Reward: Bronze Medal."
    elif score >= 0 and effort >= 0:
        result = "Needs improvement, minimal effort. Reward: Participation Certificate."
    else:
        result = "Invalid input combination. Please check your scores and effort levels."
    return result
if __name__ == '__main__':
    sample_score_1 = 95
    sample_effort_1 = 9
    sample_score_2 = 65
    sample_effort_2 = 4
    sample_score_3 = 40
    sample_effort_3 = 10
    sample_score_4 = 100
    sample_effort_4 = -5
    print(f"Scenario 1 (Score: {sample_score_1}, Effort: {sample_effort_1}): {decision_simulator(sample_score_1, sample_effort_1)}")
    print(f"Scenario 2 (Score: {sample_score_2}, Effort: {sample_effort_2}): {decision_simulator(sample_score_2, sample_effort_2)}")
    print(f"Scenario 3 (Score: {sample_score_3}, Effort: {sample_effort_3}): {decision_simulator(sample_score_3, sample_effort_3)}")
    print(f"Scenario 4 (Score: {sample_score_4}, Effort: {sample_effort_4}): {decision_simulator(sample_score_4, sample_effort_4)}")
    print(f"Scenario 5 (Score: 50, Effort: 3): {decision_simulator(50, 3)}")
    print(f"Scenario 6 (Score: 10, Effort: 1): {decision_simulator(10, 1)}")