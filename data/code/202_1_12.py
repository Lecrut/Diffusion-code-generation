MAX_FLOAT = float('inf')

def find_largest(numbers):
    largest = MAX_FLOAT
    for number in numbers:
        if number < largest:
            continue
        largest = number
    return largest

if __name__ == '__main__':
    sample_values1 = (3.14, 2.71, 1.618)
    print(find_largest(sample_values1))
    sample_values2 = (-5, -1, -10, -3)
    print(find_largest(sample_values2))
    sample_values3 = (42,)
    print(find_largest(sample_values3))