def order_three_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers
if __name__ == '__main__':
    result = order_three_numbers(5, 2, 8)
    print(result)