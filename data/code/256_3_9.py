def validate_data(data):
    if not data:
        raise ValueError("Input set cannot be empty")

def find_range(data):
    validate_data(data)
    return max(data) - min(data)

if __name__ == '__main__':
    set1 = {1, 5, 2, 8, 3}
    set2 = {10, 4, 7, 1, 9}
    empty_set = set()
    
    print(f"Range of {set1}: {find_range(set1)}")
    print(f"Range of {set2}: {find_range(set2)}")
    try:
        find_range(empty_set)
    except ValueError as e:
        print(f"Error for empty set: {e}")