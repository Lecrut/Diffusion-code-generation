def flatten_and_find_largest(nested_list):
    flattened = [num for sublist in nested_list for num in sublist]
    if not flattened:
        raise ValueError("Flattened list cannot be empty")
    largest = flattened[0]
    for number in flattened[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [[1, 5], [3, 2], [9, 4]]
    print(f"Largest in {sample_list}: {flatten_and_find_largest(sample_list)}")