import timeit
def evaluate_expression(expr: str) -> bool:
    try:
        return eval(expr, {"__builtins__": {}}, {})
    except Exception:
        return False
if __name__ == '__main__':
    sample_data = {
        "x": 10,
        "y": 20,
        "z": True
    }
    exprs = [
        "x > y and z",
        "not x or not y",
        "sample_data['a'] if 'a' in sample_data else False"
    ]
    for i, expression in enumerate(exprs):
        print(f"Evaluating: {expression}")
        result = evaluate_expression(expression)
        print(f"Result: {result}\n")
        iterations = 10000
        t = timeit.timeit(
            stmt=f'evaluate_expression("{expression}")', 
            setup='from __main__ import evaluate_expression, sample_data; x=sample_data["x"]; y=sample_data["y"]', 
            number=iterations
        )
        avg_time_per_call = t / iterations * 1000               
        print(f"Average execution time per call: {avg_time_per_call:.4f} ms")