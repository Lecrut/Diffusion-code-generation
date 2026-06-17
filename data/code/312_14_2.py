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
    result1 = find_largest(sequence1)
    print(f"Sequence: {sequence1}")
    print(f"Largest element: {result1}")
    sequence2 = [-10.5, -3.2, -5.8, -1.1]
    result2 = find_largest(sequence2)
    print(f"Sequence: {sequence2}")
    print(f"Largest element: {result2}")
    sequence3 = [1e-100, 1e-50, 1e-100]
    result3 = find_largest(sequence3)
    print(f"Sequence: {sequence3}")
    print(f"Largest element: {result3}")
    sequence4 = [99.9, 100.1, 50.0, 200.5]
    result4 = find_largest(sequence4)
    print(f"Sequence: {sequence4}")
    print(f"Largest element: {result4}")
    empty_sequence = []
    try:
        find_largest(empty_sequence)
    except ValueError as e:
        print(f"Handling empty sequence error: {e}")