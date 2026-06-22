def compare_two_simple_quantities_now_batch_process(values: list) -> list:
    results = []
    for i in range(0, len(values), 2):
        if i + 1 < len(values):
            a, b = values[i], values[i + 1]
            if a > b:
                results.append({"result": "a is greater than b", "a": a, "b": b})
            elif a < b:
                results.append({"result": "a is less than b", "a": a, "b": b})
            else:
                results.append({"result": "a is equal to b", "a": a, "b": b})
    return results

if __name__ == '__main__':
    sample_values = [10, 5, 20, 20, 30, 30]
    batch_results = compare_two_simple_quantities_now_batch_process(sample_values)
    for result in batch_results:
        print(f"Comparing {result['a']} and {result['b']}: {result}")