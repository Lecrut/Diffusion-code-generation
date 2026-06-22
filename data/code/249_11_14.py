def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for num in data[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 2, 8, 3],
        [-10, -5, -20, -1],
        [42],
        []
    ]
    for lst in sample_lists:
        try:
            print(f"Largest in {lst}: {find_largest(lst)}")
        except ValueError as e:
            print(e)