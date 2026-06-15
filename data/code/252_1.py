def compare_quantities(a, b):
    if a > b:
        return "a is greater"
    elif b > a:
        return "b is greater"
    else:
        return "the quantities are equal"
if __name__ == '__main__':
    print(compare_quantities(10, 5))
    print(compare_quantities(20, 30))
    print(compare_quantities(7, 7))
    print(compare_quantities(100, 99))