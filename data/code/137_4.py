def evaluate_complex_condition(number):
    if number > 100:
        if number % 2 == 0:
            return "Valid"
        else:
            return "Invalid"
    elif 0 <= number <= 100:
        if number % 10 == 0:
            return "Valid"
        else:
            return "Invalid"
    else:
        return "Invalid"
if __name__ == '__main__':
    test_numbers = [150, 200, 50, 100, 101, 0, -5]
    for num in test_numbers:
        result = evaluate_complex_condition(num)
        print(f"Number: {num}, Result: {result}")