def sort_numbers(a, b, c):
    numbers = [a, b, c]
    return sorted(numbers)

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    sorted_nums = sort_numbers(num1, num2, num3)
    print(*sorted_nums)