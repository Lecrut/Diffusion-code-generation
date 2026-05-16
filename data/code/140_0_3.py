def evaluate_conditions(conditions):
    state = "Unknown"
    if all(conditions):
        state = "True"
    elif any(conditions):
        state = "Partially True"
    else:
        state = "False"
    return state
if __name__ == '__main__':
    input_conditions_1 = [True, False, True]
    result_1 = evaluate_conditions(input_conditions_1)
    print(f"Input: {input_conditions_1}, Result: {result_1}")
    input_conditions_2 = [False, False, False]
    result_2 = evaluate_conditions(input_conditions_2)
    print(f"Input: {input_conditions_2}, Result: {result_2}")
    input_conditions_3 = [True, True, True]
    result_3 = evaluate_conditions(input_conditions_3)
    print(f"Input: {input_conditions_3}, Result: {result_3}")
    input_conditions_4 = [True, False, False]
    result_4 = evaluate_conditions(input_conditions_4)
    print(f"Input: {input_conditions_4}, Result: {result_4}")
    input_conditions_5 = [False, True, False]
    result_5 = evaluate_conditions(input_conditions_5)
    print(f"Input: {input_conditions_5}, Result: {result_5}")