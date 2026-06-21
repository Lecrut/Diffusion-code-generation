MAX_INT = float('inf')

def find_largest(numbers):
    if not numbers:
        return None
    largest = -MAX_INT
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    largest = find_largest(sample_list)
    print(largest)