MAX_VALUE = 99

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = (99, 45, 67, 12, 88)
    result = find_largest(sample_values)
    print(result)