def compare_two_simple_quantities_now_validate(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return max(a, b)

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_validate(3, 5)
    print(result)