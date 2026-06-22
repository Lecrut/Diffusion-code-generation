def compare_two_simple_quantities_now_batch_process(samples: list) -> list:
    results = []
    for a, b in samples:
        if a > b:
            result = {"result": "a is greater than b", "a": a, "b": b}
        elif a < b:
            result = {"result": "a is less than b", "a": a, "b": b}
        else:
            result = {"result": "a is equal to b", "a": a, "b": b}
        results.append(result)
    return results

if __name__ == '__main__':
    samples = [(10, 5), (20, 20), (30, 40)]
    results = compare_two_simple_quantities_now_batch_process(samples)
    for result in results:
        print(f"Comparing {result['a']} and {result['b']}: {result}")