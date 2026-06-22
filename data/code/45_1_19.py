def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_min(sample_list))