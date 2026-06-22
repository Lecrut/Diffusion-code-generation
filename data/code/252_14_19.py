def compare_two_simple_quantities_now_run_examples():
    examples = [
        (5, 3),
        (2, 8),
        (10, 10)
    ]
    
    for a, b in examples:
        if a > b:
            result = f"{a} is greater than {b}"
        elif a < b:
            result = f"{a} is less than {b}"
        else:
            result = f"{a} is equal to {b}"
        
        print(result)

if __name__ == '__main__':
    compare_two_simple_quantities_now_run_examples()