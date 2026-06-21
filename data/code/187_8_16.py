MAX_INT = float('inf')

def find_largest(data):
    if not data:
        return None
    largest = -MAX_INT
    for num in data:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_largest(sample_list)
    print(f"List: {sample_list}, Largest element: {result}")