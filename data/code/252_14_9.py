def compare_two_simple_quantities_now_run_examples():
    examples = [
        (3, 5),
        (10, 2),
        (7, 7),
        (0, 0),
        (-1, -5)
    ]
    
    for a, b in examples:
        result = max(a, b)
        print(f"max({a}, {b}) = {result}")

if __name__ == '__main__':
    compare_two_simple_quantities_now_run_examples()