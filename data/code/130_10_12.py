def is_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = {
        0: True,
        5: False,
        -0: True,
        3.14: False,
        '0': False
    }
    
    for value, expected in test_values.items():
        result = is_zero(value)
        print(f"is_zero({value}): {result} (Expected: {expected})")