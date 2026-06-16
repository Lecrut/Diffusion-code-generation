def find_largest(data):
    if not data:
        raise ValueError("Input sequence cannot be empty")
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    sequence1 = [3.14, 1.618, 2.718, 0.577, 4.0]
    sequence2 = [-10.5, -5.2, -20.1, -1.0, -3.3]
    sequence3 = [1.0]
    sequence4 = [99.99999999999999]
    print(f"Largest in {sequence1}: {find_largest(sequence1)}")
    print(f"Largest in {sequence2}: {find_largest(sequence2)}")
    print(f"Largest in {sequence3}: {find_largest(sequence3)}")
    print(f"Largest in {sequence4}: {find_largest(sequence4)}")