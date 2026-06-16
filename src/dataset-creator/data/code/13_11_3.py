def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
if __name__ == '__main__':
    sample_data = [3, 7, -5, 2.5, 9, 4.8, 0]
    result = find_largest(sample_data)
    print(result)