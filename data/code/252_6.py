def find_min_max(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    result = find_min_max(num1, num2)
    print(result)