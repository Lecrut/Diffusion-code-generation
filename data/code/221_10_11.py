def sort_numbers(a, b, c):
    try:
        numbers = [a, b, c]
        numbers.sort()
        return numbers
    except TypeError as e:
        print(f"Error: All inputs must be integers. {e}")
        return None

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    sorted_nums = sort_numbers(num1, num2, num3)
    if sorted_nums:
        print(*sorted_nums)