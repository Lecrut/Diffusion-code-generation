import sys
def process_conditions(conditions):
    result = 0
    for condition in conditions:
        if condition == "A":
            result += 1
        elif condition == "B":
            result -= 1
    return result
if __name__ == '__main__':
    sample_input = ["A", "B", "A", "C", "B"]
    input_conditions = sample_input
    derived_outcome = process_conditions(input_conditions)
    print(derived_outcome)