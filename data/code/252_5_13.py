def compare_quantities(a, b):
    if a > b:
        return "a is greater"
    elif a < b:
        return "b is greater"
    else:
        return "a and b are equal"

if __name__ == '__main__':
    print(compare_quantities(5, 3))
    print(compare_quantities(10, 10))
    print(compare_quantities(2, 4))