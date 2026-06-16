import timeit
def evaluate_expression(expr: str, mapping: dict) -> bool:
    return eval(expr, {"__builtins__": {}}, mapping)
if __name__ == '__main__':
    sample_mapping = {
        "a": 10,
        "b": 20,
        "c": True,
        "d": False
    }
    test_exprs = [
        "a > b and c",
        "not d or a == 5",
        "(a + b) < 31"
    ]
    iterations = 10000
    for expr in test_exprs:
        start_time = timeit.default_timer()
        result = evaluate_expression(expr, sample_mapping)
        end_time = timeit.default_timer()
        print(f"Expression: {expr}")
        print(f"Result: {result}")
        print(f"Execution Time (approx): {(end_time - start_time) * 1000:.2f} ms\n")