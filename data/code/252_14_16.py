def compare_two_simple_quantities_now_run_examples():
    examples = [
        (5, 3),
        (10, 10),
        (2, 8)
    ]
    
    for a, b in examples:
        result = "a > b" if a > b else "a <= b"
        print(f"a: {a}, b: {b}, Result: {result}")

if __name__ == '__main__':
    compare_two_simple_quantities_now_run_examples()