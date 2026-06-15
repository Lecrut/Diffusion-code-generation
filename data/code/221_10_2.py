import sys
def sort_three_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[0], numbers[1], numbers[2]
if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 8
    sorted_nums = sort_three_numbers(num1, num2, num3)
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")