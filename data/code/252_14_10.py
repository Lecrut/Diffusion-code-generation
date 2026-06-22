def compare_two_simple_quantities_now_run_examples():
    examples = [
        (5, 3),
        (10, 10),
        (2, 8)
    ]
    
    results = []
    for a, b in examples:
        if a > b:
            result = "a is greater than b"
        elif a < b:
            result = "a is less than b"
        else:
            result = "a is equal to b"
        results.append((a, b, result))
    
    return results

if __name__ == '__main__':
    print(compare_two_simple_quantities_now_run_examples())