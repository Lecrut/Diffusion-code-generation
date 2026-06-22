def validate_input(lst, indices):
    if not isinstance(lst, list):
        raise ValueError("The first argument must be a list.")
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
    sample_list = [5, 15, 25, 35, 45]
    sample_indices = [-1, 0, 2, 4, 6]
    print(access_list_elements(sample_list, sample_indices))