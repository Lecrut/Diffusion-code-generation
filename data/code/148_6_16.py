MAX_INT = float('inf')

def find_largest(data):
    if not data:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = -MAX_INT
    for item in data:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_sequence1 = [3, 5, 1, 8, 2]
    print(f"The largest element in {sample_sequence1} is: {find_largest(sample_sequence1)}")
    
    sample_sequence2 = [-10, -5, -20]
    print(f"The largest element in {sample_sequence2} is: {find_largest(sample_sequence2)}")
    
    sample_sequence3 = []
    try:
        print(find_largest(sample_sequence3))
    except ValueError as e:
        print(f"Error for empty list: {e}")