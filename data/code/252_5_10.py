def compare_quantities(a, b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"

if __name__ == '__main__':
    print(compare_quantities(5, 3))
    print(compare_quantities(10, 10))
    print(compare_quantities(2, 8))