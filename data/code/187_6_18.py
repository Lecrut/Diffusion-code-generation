MAX_VALUE = float('-inf')

def find_largest_number(numbers):
    largest = MAX_VALUE
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Largest number in sample list:", find_largest_number(sample_list))
    large_sample = [100, 50, 200, 10, 300, 150]
    print("Largest number in large sample list:", find_largest_number(large_sample))