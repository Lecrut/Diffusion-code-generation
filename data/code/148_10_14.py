MAX_INT = float('inf')

def find_largest(numbers):
    if not numbers:
        return None
    largest = -MAX_INT
    for num in numbers:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    largest = find_largest(sample_list)
    print(largest)