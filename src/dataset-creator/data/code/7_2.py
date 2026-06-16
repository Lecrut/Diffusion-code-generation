def evaluate_simple_true_false(statement):
    return eval(statement) if not isinstance(statement, str) else False
def compare_strings(str1, str2):
    return str1 == str2
def compare_variables(var_a, var_b):
    return var_a == var_b
def check_numeric_equality(num1, num2):
    return num1 == num2
if __name__ == '__main__':
    sample_strings = "hello", "world"
    sample_vars = 42, 3.14
    print(compare_strings(sample_strings[0], sample_strings[1]))
    print(compare_variables(sample_vars[0], sample_vars[1]))