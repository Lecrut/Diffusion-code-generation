def compare_two_simple_quantities_now_run_examples():
    examples = [
        (5, 3),
        (10, 10),
        (2, 8)
    ]
    
    results = []
    for a, b in examples:
        if a > b:
            result = f"{a} is greater than {b}"
        elif a < b:
            result = f"{a} is less than {b}"
        else:
            result = f"{a} is equal to {b}"
        results.append(result)
    
    return results

if __name__ == '__main__':
    outputs = compare_two_simple_quantities_now_run_examples()
    for output in outputs:
        print(output)