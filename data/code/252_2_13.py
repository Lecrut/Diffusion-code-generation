def compare_two_simple_quantities_now_batch_process(values: list) -> list:
    results = []
    for a, b in values:
        if a > b:
            result = {"result": "a is greater than b", "a": a, "b": b}
        elif a < b:
            result = {"result": "a is less than b", "a": a, "b": b}
        else:
            result = {"result": "a is equal to b", "a": a, "b": b}
        results.append(result)
    return results

if __name__ == '__main__':
    sample_values = [(10, 5), (20, 20), (30, 15)]
    processed_results = compare_two_simple_quantities_now_batch_process(sample_values)
    for result in processed_results:
        print(result)