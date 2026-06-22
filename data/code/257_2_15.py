def abs_diff(a, b):
    diff = a - b
    return (diff ^ (diff >> 31)) >> 31

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = abs_diff(num1, num2)
    print(result)