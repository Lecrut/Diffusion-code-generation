def sort_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    sample_values = {1: 15, 2: 7, 3: 22}
    num1 = sample_values[1]
    num2 = sample_values[2]
    num3 = sample_values[3]
    sorted_nums = sort_numbers(num1, num2, num3)
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")