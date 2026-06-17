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
    sequence2 = [-10.5, -5.2, -8.9, -1.1, -3.3]
    print(f"\nSequence 2: {sequence2}")
    print(f"Largest element in Sequence 2: {find_largest(sequence2)}")
    sequence3 = [100.0, -50.0, 200.0, 75.0]
    print(f"\nSequence 3: {sequence3}")
    print(f"Largest element in Sequence 3: {find_largest(sequence3)}")
    sequence4 = [42.0]
    print(f"\nSequence 4: {sequence4}")
    print(f"Largest element in Sequence 4: {find_largest(sequence4)}")
    sequence5 = []
    try:
        print(f"\nSequence 5: {sequence5}")
        print(f"Largest element in Sequence 5: {find_largest(sequence5)}")
    except ValueError as e:
        print(f"Error for Sequence 5: {e}")