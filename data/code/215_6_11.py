MAX_FLOAT = float('-inf')

def find_largest_number(numbers):
    largest = MAX_FLOAT
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.41, 9.81, 6.28]
    print(find_largest_number(sample_values))