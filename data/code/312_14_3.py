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
    print(f"Sequence 1: {sequence1}")
    print(f"Largest element in Sequence 1: {find_largest(sequence1)}")
    sequence2 = [-10.5, -3.2, -8.9, -0.1, -5.5]
    print(f"\nSequence 2: {sequence2}")
    print(f"Largest element in Sequence 2: {find_largest(sequence2)}")
    sequence3 = [100.0, 50.5, 200.1, 75.3]
    print(f"\nSequence 3: {sequence3}")
    print(f"Largest element in Sequence 3: {find_largest(sequence3)}")
    sequence4 = [42.0]
    print(f"\nSequence 4: {sequence4}")
    print(f"Largest element in Sequence 4: {find_largest(sequence4)}")
    try:
        empty_sequence = []
        print(f"\nSequence Empty: {empty_sequence}")
        find_largest(empty_sequence)
    except ValueError as e:
        print(f"Error caught for empty sequence: {e}")