def compare_two_simple_quantities_now_batch_process(values):
    results = []
    for i in range(len(values) // 2):
        a, b = values[i * 2], values[i * 2 + 1]
        if a > b:
            results.append({"result": "a is greater than b", "a": a, "b": b})
        elif a < b:
            results.append({"result": "a is less than b", "a": a, "b": b})
        else:
            results.append({"result": "a is equal to b", "a": a, "b": b})
    return results

if __name__ == '__main__':
    sample_values = [10, 5, 20, 20, 30, 15]
    comparison_results = compare_two_simple_quantities_now_batch_process(sample_values)
    for result in comparison_results:
        print(f"Comparing {result['a']} and {result['b']}: {result}")