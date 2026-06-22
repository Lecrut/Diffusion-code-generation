def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for num in data[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_values = {
        "list1": [1, 5, 2, 8, 3],
        "list2": [-10, -5, -20, -1],
        "list3": [42]
    }
    
    for key, value in sample_values.items():
        try:
            print(f"Largest in {key}: {find_largest(value)}")
        except ValueError as e:
            print(e)