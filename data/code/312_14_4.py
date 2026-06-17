def find_largest_element(data):
    if not data:
        raise ValueError("Input sequence cannot be empty")
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    sequence1 = [3.14, 1.618, 2.718, 0.577, 4.0]
    sequence2 = [-10.5, -5.2, -20.1, -1.9]
    sequence3 = [1.0, 1.0, 1.0, 1.0, 1.0]
    large_sequence = [1e-100, 5.0, -999.9999999999999, 3.141592653589793, 12345.6789]
    print(f"Largest in {sequence1}: {find_largest_element(sequence1)}")
    print(f"Largest in {sequence2}: {find_largest_element(sequence2)}")
    print(f"Largest in {sequence3}: {find_largest_element(sequence3)}")
    print(f"Largest in large_sequence: {find_largest_element(large_sequence)}")