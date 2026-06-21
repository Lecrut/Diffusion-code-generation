def validate_input(lst, indices):
    if not isinstance(lst, list):
        raise ValueError("The first argument must be a list.")
    if not all(isinstance(i, int) for i in lst):
        raise ValueError("All elements of the first argument must be integers.")
    if not isinstance(indices, list):
        raise ValueError("The second argument must be a list.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements of the second argument must be integers.")

def access_list_elements(lst, indices):
    validate_input(lst, indices)
    result = []
    for index in indices:
        try:
            result.append(lst[index])
        except IndexError:
            continue
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 3, 4, 7, -2]
    print(access_list_elements(sample_list, sample_indices))