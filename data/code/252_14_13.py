def compare_two_simple_quantities_now_run_examples():
    examples = [
        (3, 5),
        (10, 2),
        (7, 7),
        (0, -1),
        (-5, -3)
    ]
    
    for a, b in examples:
        result = max(a, b) if a > b else min(a, b)
        print(f"Comparing {a} and {b}: {result}")

if __name__ == '__main__':
    compare_two_simple_quantities_now_run_examples()