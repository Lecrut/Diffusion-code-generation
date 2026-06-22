def access_list_elements(lst, indices):
    def validate_input():
        if not isinstance(lst, list):
            raise ValueError("The first argument must be a list.")
        if not all(isinstance(i, int) for i in lst):
            raise ValueError("All elements of the first argument must be integers.")
        if not isinstance(indices, list):
            raise ValueError("The second argument must be a list.")
        if not all(isinstance(i, int) for i in indices):
            raise ValueError("All elements of the second argument must be integers.")

    validate_input()
    
    result = []
    for index in indices:
        try:
            result.append(lst[index])
        except IndexError:
            continue
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6, -1]
    print(access_list_elements(sample_list, sample_indices))