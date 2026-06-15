def compare_numbers(a, b):
    if a > b:
        return f"{a} is larger than {b}"
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"{a} and {b} are equal"
if __name__ == '__main__':
    print(compare_numbers(10, 5))
    print(compare_numbers(20, 30))
    print(compare_numbers(7, 7))
    print(compare_numbers(-5, 12))
    print(compare_numbers(0, -1))