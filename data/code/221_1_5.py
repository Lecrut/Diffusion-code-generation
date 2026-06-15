def order_three_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers
if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 9
    sorted_numbers = order_three_numbers(num1, num2, num3)
    print(sorted_numbers)