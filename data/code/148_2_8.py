def find_largest_element(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [3.5, 6.7, 2.8, 9.1, 4.2]
    print(find_largest_element(sample_data))