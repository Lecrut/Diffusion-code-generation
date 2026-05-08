import sys
def decision_simulator(score, age):
    if score >= 90 and age >= 65:
        result = "Senior Citizen Bonus"
    elif score >= 70 or age >= 60:
        result = "Mid-Range Incentive"
    elif score >= 50:
        result = "Standard Qualification"
    elif score >= 30:
        result = "Low Qualification"
    else:
        result = "Insufficient Qualification"
    return result
def process_input(input_score, input_age):
    try:
        score = int(input_score)
        age = int(input_age)
    except ValueError:
        return "Error: Invalid input. Please provide integer values."
    if score < 0 or age < 0:
        return "Error: Score and age must be non-negative."
    return decision_simulator(score, age)
if __name__ == '__main__':
    sample_score_1 = "95"
    sample_age_1 = "70"
    sample_score_2 = "45"
    sample_age_2 = "30"
    sample_score_3 = "80"
    sample_age_3 = "55"
    sample_score_4 = "100"
    sample_age_4 = "25"
    sample_score_5 = "20"
    sample_age_5 = "50"
    print(f"Scenario 1 (Score: {sample_score_1}, Age: {sample_age_1}): {process_input(sample_score_1, sample_age_1)}")
    print(f"Scenario 2 (Score: {sample_score_2}, Age: {sample_age_2}): {process_input(sample_score_2, sample_age_2)}")
    print(f"Scenario 3 (Score: {sample_score_3}, Age: {sample_age_3}): {process_input(sample_score_3, sample_age_3)}")
    print(f"Scenario 4 (Score: {sample_score_4}, Age: {sample_age_4}): {process_input(sample_score_4, sample_age_4)}")
    print(f"Scenario 5 (Score: {sample_score_5}, Age: {sample_age_5}): {process_input(sample_score_5, sample_age_5)}")
    print(f"Scenario 6 (Invalid Input Test): {process_input('abc', '30')}")
    print(f"Scenario 7 (Negative Input Test): {process_input(-10, 50)}")