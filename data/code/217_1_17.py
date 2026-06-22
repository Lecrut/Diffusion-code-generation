def is_valid_number(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    return True

def compare_numbers(a, b):
    is_valid_number(a)
    is_valid_number(b)
    if a > b:
        return True
    else:
        return False

if __name__ == '__main__':
    print(compare_numbers(10, 5))
    print(compare_numbers(20, 30))
    print(compare_numbers(7, 7))
    print(compare_numbers(-5, 12))
    print(compare_numbers(0, -1))