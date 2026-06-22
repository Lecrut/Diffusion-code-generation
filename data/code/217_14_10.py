def compare_integers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    print(compare_integers(10, 5))
    print(compare_integers(3, 8))
    print(compare_integers(7, 7))