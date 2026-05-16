import sys
def process_conditions(conditions):
    result = "No conditions provided."
    if "A" in conditions and "B" in conditions:
        result = "Condition A and B met."
    elif "A" in conditions:
        result = "Only Condition A met."
    elif "B" in conditions:
        result = "Only Condition B met."
    else:
        result = "No specific conditions met."
    return result
if __name__ == '__main__':
    sample_input_line = "A B"
    input_conditions = set(sample_input_line.split())
    output = process_conditions(input_conditions)
    print(output)