def reverse_numbers(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = reverse_numbers(num1, num2)
    print(result)