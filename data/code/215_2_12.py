MAX_VALUE = 300

def find_largest_integer(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [100, 200, 50, 300, 75]
    result = find_largest_integer(sample_numbers)
    print(result)