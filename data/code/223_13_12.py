def find_largest_number(numbers):
    if not numbers:
        return float('-inf')
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample1 = [3, 9, 1, 5, 2]
    result1 = find_largest_number(sample1)
    print(f"Maximum of {sample1}: {result1}")

    sample2 = [-7, -3, -10, -4]
    result2 = find_largest_number(sample2)
    print(f"Maximum of {sample2}: {result2}")