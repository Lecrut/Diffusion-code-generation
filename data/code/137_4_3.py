def evaluate_complex_condition(number):
    if number > 0 and number % 2 == 0:
        if number < 100:
            return "Valid"
        else:
            return "Invalid"
    elif number > 100 and number % 3 == 0:
        return "Valid"
    else:
        return "Invalid"
if __name__ == '__main__':
    test_numbers = [2, 4, 100, 101, 150, 3]
    for num in test_numbers:
        result = evaluate_complex_condition(num)
        print(f"Number: {num}, Result: {result}")