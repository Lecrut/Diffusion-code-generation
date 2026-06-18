def evaluate_statement(statement: str) -> bool:
    try:
        return eval(statement)
    except Exception:
        return False
def compare_strings(str1: str, str2: str) -> bool:
    return str1 == str2
def compare_variables(var_a: any, var_b: any) -> bool:
    return var_a == var_b
if __name__ == '__main__':
    sample_statements = [
        "x > 5",
        "'hello' == 'world'",
        "[1, 2] == [3]",
        "True and True"
    ]
    variables_x = 6
    variables_y = 7
    print(evaluate_statement("variables_x > 5"))
    print(compare_strings("test", "TEST"))
    print(compare_variables(variables_x, variables_y))