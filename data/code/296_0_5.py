import math
def change_ratio_scenario_one(a, b, c):
    new_ratio = (a * 2) / b
    return new_ratio
def change_ratio_scenario_two(a, b, c):
    new_ratio = (a + b) / c
    return new_ratio
def change_ratio_scenario_three(a, b, c):
    new_ratio = (a * b) / (c - 1)
    return new_ratio
if __name__ == '__main__':
    sample_a = 10
    sample_b = 4
    sample_c = 5
    print("--- Scenario 1: Doubling one part of the ratio ---")
    result1 = change_ratio_scenario_one(sample_a, sample_b, sample_c)
    print(f"Original values: A={sample_a}, B={sample_b}, C={sample_c}")
    print(f"Calculated new ratio (A*2 / B): {result1}")
    print("\n--- Scenario 2: Summing two parts and dividing by the third ---")
    result2 = change_ratio_scenario_two(sample_a, sample_b, sample_c)
    print(f"Original values: A={sample_a}, B={sample_b}, C={sample_c}")
    print(f"Calculated new ratio ((A + B) / C): {result2}")
    print("\n--- Scenario 3: Multiplying two parts and subtracting one from the third ---")
    result3 = change_ratio_scenario_three(sample_a, sample_b, sample_c)
    print(f"Original values: A={sample_a}, B={sample_b}, C={sample_c}")
    print(f"Calculated new ratio ((A * B) / (C - 1)): {result3}")