def sort_floats(a, b):
    if a <= b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    num1 = 3.14
    num2 = 2.71
    result = sort_floats(num1, num2)
    print(result)