def validate_lists(*lists):
    if not all(isinstance(lst, list) for lst in lists):
        raise ValueError("All inputs must be lists")
    if any(not all(isinstance(item, (int, str)) for item in lst) for lst in lists):
        raise ValueError("Lists can only contain integers and strings")

def find_duplicates(*lists):
    validate_lists(*lists)
    sets = [set(lst) for lst in lists]
    intersection = set.intersection(*sets)
    return list(intersection)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [4, 5, 7, 8]
    ]
    duplicates = find_duplicates(*sample_lists)
    print(duplicates)