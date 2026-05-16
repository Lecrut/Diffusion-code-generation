def evaluate_expression(expression, var1_name, var2_name, values):
    var1 = values[var1_name]
    var2 = values[var2_name]
    if "AND" in expression:
        result = var1 and var2
    elif "OR" in expression:
        result = var1 or var2
    elif "NOT" in expression:
        pass
    else:
        result = False
    return result
def generate_truth_table(expression, var1_name, var2_name, sample_values):
    results = []
    num_rows = 2 ** 2
    truth_combinations = [
        (False, False),
        (False, True),
        (True, False),
        (True, True)
    ]
    for v1, v2 in truth_combinations:
        eval_expression = expression.replace(var1_name, str(v1)).replace(var2_name, str(v2))
        try:
            result = eval(eval_expression)
            results.append((v1, v2, result))
        except Exception:
            results.append((v1, v2, "Error"))
    return results
if __name__ == '__main__':
    expression = "V1 AND V2"
    var1_name = "V1"
    var2_name = "V2"
    sample_values = {
        var1_name: False,
        var2_name: False
    }
    truth_table = generate_truth_table(expression, var1_name, var2_name, sample_values)
    print("Truth Table for Expression:")
    print("------------------------------")
    print(f"{var1_name}\t{var2_name}\tResult")
    print("------------------------------")
    for v1, v2, result in truth_table:
        print(f"{v1}\t{v2}\t{result}")