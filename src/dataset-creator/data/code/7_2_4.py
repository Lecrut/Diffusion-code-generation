def evaluate_simple_true_false(statement: str) -> bool:
    return eval(statement)
def compare_strings(str1: str, str2: str) -> bool:
    return str1 == str2
def compare_variables(var_a, var_b) -> bool:
    return var_a == var_b
if __name__ == '__main__':
    sample_statement = "5 + 3 > 7"
    result_simple = evaluate_simple_true_false(sample_statement)
    str_val1 = "hello"
    str_val2 = "world"
    res_str_compare = compare_strings(str_val1, str_val2)
    var_x = 10
    var_y = 5
    res_var_compare = compare_variables(var_x, var_y * 2)
    print(f"Simple Statement Result: {result_simple}")
    print(f"String Comparison Result: {res_str_compare}")
    print(f"Variable Comparison Result: {res_var_compare}")