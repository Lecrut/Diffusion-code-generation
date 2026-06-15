def find_middle(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 20
    middle_value = find_middle(num1, num2, num3)
    print(middle_value)