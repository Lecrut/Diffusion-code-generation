def is_valid_sample(sample):
    if not isinstance(sample, (int, float)):
        return False
    if sample <= 0:
        return False
    return True

def compare_two_simple_quantities_now_filter_valid(a, b):
    if not is_valid_sample(a) or not is_valid_sample(b):
        raise ValueError("Both samples must be positive numbers.")
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"

if __name__ == '__main__':
    num1 = 15
    num2 = 25
    result = compare_two_simple_quantities_now_filter_valid(num1, num2)
    print(result)
    
    num3 = -5
    try:
        result2 = compare_two_simple_quantities_now_filter_valid(num3, num2)
        print(result2)
    except ValueError as e:
        print(e)

    num4 = 0.5
    result3 = compare_two_simple_quantities_now_filter_valid(num1, num4)
    print(result3)