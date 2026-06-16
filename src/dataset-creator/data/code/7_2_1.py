def evaluate_simple_statement(statement: str) -> bool:
    try:
        result = eval(statement, {"__builtins__": {}}, {})
        return isinstance(result, bool) and (result is True or result is False)
    except Exception:
        raise ValueError("Invalid expression")
def compare_strings(str1: str, str2: str) -> bool:
    return str1 == str2
def check_variable_equality(var_a: any, var_b: any) -> bool:
    return var_a == var_b
if __name__ == '__main__':
    sample_statements = [
        "5 + 3 > 19",
        "'hello' == 'world'",
        "{1, 2} & {2, 3}",
        "[1, 2] in [[1], [2]]"
    ]
    variables_a = {"x": 10, "y": 5.0}
    variables_b = {"z": 10, "w": 6.0}
    print(evaluate_simple_statement("5 + 3 > 19"))
    print(compare_strings("hello", "world"))
    print(check_variable_equality(variables_a["x"], variables_b["z"]))