def evaluate_complex_condition(number, age, has_license, is_adult):
    if number > 18 and age >= 18 and has_license and is_adult:
        return "Valid"
    else:
        return "Invalid"
if __name__ == '__main__':
    print(evaluate_complex_condition(25, 20, True, True))
    print(evaluate_complex_condition(16, 20, True, True))
    print(evaluate_complex_condition(30, 15, True, True))
    print(evaluate_complex_condition(20, 18, False, True))
    print(evaluate_complex_condition(10, 18, True, False))
    print(evaluate_complex_condition(18, 18, False, True))