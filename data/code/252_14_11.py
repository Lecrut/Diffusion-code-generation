def compare_two_simple_quantities_now_run_examples():
    examples = [
        (5, 3),
        (10, 10),
        (-2, -5),
        (0, 0),
        (7.5, 7.5)
    ]
    
    results = []
    for a, b in examples:
        if a > b:
            result = "greater"
        elif a < b:
            result = "less"
        else:
            result = "equal"
        results.append((a, b, result))
    
    return results

if __name__ == '__main__':
    print(compare_two_simple_quantities_now_run_examples())