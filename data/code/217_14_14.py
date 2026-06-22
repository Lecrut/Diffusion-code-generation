def compare_integers(a, b):
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    print(compare_integers(5, 3))
    print(compare_integers(10, 10))
    print(compare_integers(7, 9))