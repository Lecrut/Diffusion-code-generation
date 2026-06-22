def validate_numbers(a, b, c):
    if not all(isinstance(x, int) for x in (a, b, c)):
        raise ValueError("All inputs must be integers")
    if len(set([a, b, c])) != 3:
        raise ValueError("Inputs must be distinct")

def sort_three_numbers(a, b, c):
    validate_numbers(a, b, c)
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    num1 = 5
    num2 = 1
    num3 = 8
    sorted_nums = sort_three_numbers(num1, num2, num3)
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")