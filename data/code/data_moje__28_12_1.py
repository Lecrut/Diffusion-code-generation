def sort_two_numbers(a, b):
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    num1 = 3.14
    num2 = 2.71
    result = sort_two_numbers(num1, num2)
    print(result)