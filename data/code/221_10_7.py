def sort_numbers(a, b, c):
    numbers = [a, b, c]
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All inputs must be integers or floats")
    return sorted(numbers)

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    num3 = 7
    try:
        sorted_nums = sort_numbers(num1, num2, num3)
        print(*sorted_nums)
    except ValueError as e:
        print(e)