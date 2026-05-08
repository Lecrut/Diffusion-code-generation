def solve_truth_table(inputs, rule):
    if not inputs:
        return None
    num_inputs = len(inputs)
    output_values = []
    for i in range(2**num_inputs):
        input_tuple = []
        temp = i
        for _ in range(num_inputs):
            input_tuple.append(temp % 2)
            temp //= 2
        input_tuple.reverse()
        condition_met = True
        output = None
        for input_val in input_tuple:
            if input_val == 1:
                if rule[0] == 'AND':
                    if not (input_val == 1 and rule[1] == 'AND'):
                        condition_met = False
                        break
                elif rule[0] == 'OR':
                    if not (input_val == 1 or rule[1] == 'OR'):
                        condition_met = False
                        break
                elif rule[0] == 'NOT':
                    if not (input_val == 1 and rule[1] == 'NOT'):
                        condition_met = False
                        break
            else:
                if rule[0] == 'AND':
                    if not (input_val == 0 or rule[1] == 'AND'):
                        condition_met = False
                        break
                elif rule[0] == 'OR':
                    if not (input_val == 0 or rule[1] == 'OR'):
                        condition_met = False
                        break
                elif rule[0] == 'NOT':
                    if not (input_val == 0 and rule[1] == 'NOT'):
                        condition_met = False
                        break
        if condition_met:
            output = 1
        else:
            output = 0
        output_values.append(output)
    return output_values
if __name__ == '__main__':
    input_values = [0, 0, 0, 0, 1, 1, 1, 1]
    logic_rule = ['AND', 1]
    results = solve_truth_table(input_values, logic_rule)
    print(f"Inputs: {input_values}")
    print(f"Rule: {logic_rule}")
    print(f"Outputs: {results}")