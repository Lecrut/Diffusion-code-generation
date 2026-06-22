def sort_numbers(a, b, c):
    numbers = [a, b, c]
    return sorted(numbers)

if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 8
    sorted_nums = sort_numbers(num1, num2, num3)
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")