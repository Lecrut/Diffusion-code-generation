MAX_FLOAT = float('inf')

def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = -MAX_FLOAT
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [15.5, 8.2, 22.7, 4.9, 30.1, 11.3]
    result = find_largest(sample_list)
    print(result)