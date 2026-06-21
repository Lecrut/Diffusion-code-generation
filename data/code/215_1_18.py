def find_largest(numbers):
    if not numbers:
        raise ValueError("The tuple is empty")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_tuple = (99, 45, 67, 12, 88)
    result = find_largest(sample_tuple)
    print(result)