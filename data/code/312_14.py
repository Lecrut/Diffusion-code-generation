def find_largest(data):
    if not data:
        raise ValueError("Input sequence cannot be empty")
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    sequence = [3.14, 1.618, 2.718, 0.577, 9.999, -1.234, 5.0]
    largest_element = find_largest(sequence)
    print(largest_element)