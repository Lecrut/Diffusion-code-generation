def determine_sign(number):
    if number > 0:
        sign_value = 1
    elif number < 0:
        sign_value = -1
    else:
        sign_value = 0
    if sign_value == 1:
        return "positive"
    if sign_value == -1:
        return "negative"
    return "zero"

if __name__ == '__main__':
    test_values = [15, -20, 0]
    for val in test_values:
        result = determine_sign(val)
        print(result)