def compare_two_simple_quantities_now_transform(a, b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "b is greater than a"
    else:
        return "a is equal to b"

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_transform(5, 3)
    print(result)