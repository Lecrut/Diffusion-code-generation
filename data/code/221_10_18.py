def sort_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    return sorted_numbers

if __name__ == '__main__':
    NUM1 = 5
    NUM2 = 1
    NUM3 = 8
    sorted_nums = sort_numbers(NUM1, NUM2, NUM3)
    print(f"{sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}")