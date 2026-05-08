def evaluate_complex_condition(number):
    if number > 0:
        if number % 2 == 0:
            if number < 100:
                return "Valid"
            else:
                return "Invalid"
        else:
            return "Invalid"
    else:
        return "Invalid"
if __name__ == '__main__':
    test_numbers = [10, 20, 50, 100, 15, 2, 101, -5, 0]
    for num in test_numbers:
        result = evaluate_complex_condition(num)
        print(f"Number: {num}, Result: {result}")