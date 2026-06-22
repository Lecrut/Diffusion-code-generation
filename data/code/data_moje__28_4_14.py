def sort_reverse(a, b):
    values = [a, b]
    values.sort(reverse=True)
    return values

if __name__ == '__main__':
    num1 = 42
    num2 = 17
    result = sort_reverse(num1, num2)
    print(result)