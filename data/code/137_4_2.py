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
    print(evaluate_complex_condition(50))
    print(evaluate_complex_condition(100))
    print(evaluate_complex_condition(150))
    print(evaluate_complex_condition(10))
    print(evaluate_complex_condition(0))
    print(evaluate_complex_condition(-10))