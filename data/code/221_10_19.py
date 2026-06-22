def sort_integers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    num1 = 10
    num2 = 3
    num3 = 7
    result = sort_integers(num1, num2, num3)
    print(*result)