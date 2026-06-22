def compare_two_simple_quantities_now_run_examples():
    samples = [
        (42, 100),
        (50, 30),
        (75, 75)
    ]
    
    for num1, num2 in samples:
        print(f"Comparing {num1} and {num2}:")
        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num1 < num2:
            print(f"{num1} is less than {num2}")
        else:
            print(f"{num1} is equal to {num2}")

if __name__ == '__main__':
    compare_two_simple_quantities_now_run_examples()