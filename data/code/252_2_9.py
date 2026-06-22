def compare_two_simple_quantities_now_batch_process(values: list) -> list:
    results = []
    for i in range(0, len(values), 2):
        if len(values) - i < 2:
            raise ValueError("List must contain pairs of values")
        a, b = values[i], values[i + 1]
        if a > b:
            result = {"result": "a is greater than b", "a": a, "b": b}
        elif a < b:
            result = {"result": "a is less than b", "a": a, "b": b}
        else:
            result = {"result": "a is equal to b", "a": a, "b": b}
        results.append(result)
    return results

if __name__ == '__main__':
    sample_values = [10, 5, 20, 20, 30, 40]
    results = compare_two_simple_quantities_now_batch_process(sample_values)
    for result in results:
        print(f"Comparing {result['a']} and {result['b']}: {result}")