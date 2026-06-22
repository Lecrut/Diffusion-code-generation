def compare_two_simple_quantities_now_batch_process(pairs):
    results = []
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError("Each pair must contain exactly two elements")
        a, b = pair
        if a > b:
            result = "greater"
        elif a < b:
            result = "less"
        else:
            result = "equal"
        results.append({"a": a, "b": b, "result": result})
    return results

if __name__ == '__main__':
    pairs = [(10, 5), (20, 20), (30, 40)]
    results = compare_two_simple_quantities_now_batch_process(pairs)
    for result in results:
        print(f"Comparing {result['a']} and {result['b']}: {result['result']}")