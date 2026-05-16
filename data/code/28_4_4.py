def is_larger(a, b):
    return a > b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = is_larger(num1, num2)
    print(f"{num1} > {num2}: {result1}")
    num3 = 3
    num4 = 7
    result2 = is_larger(num3, num4)
    print(f"{num3} > {num4}: {result2}")
    num5 = 10
    num6 = 10
    result3 = is_larger(num5, num6)
    print(f"{num5} > {num6}: {result3}")