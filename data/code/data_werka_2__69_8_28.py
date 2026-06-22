def access_list_elements(lst, indices):
    if not isinstance(lst, list) or not all(isinstance(i, int) for i in lst):
        raise ValueError("The first argument must be a list of integers.")
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise ValueError("The second argument must be a list of integers.")
    
    def safe_access(lst, index):
        try:
            return lst[index]
        except IndexError:
            return None
    
    result = [safe_access(lst, index) for index in indices]
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices_1 = [0, 2, 4, 6, -1]
    sample_indices_2 = [1, 3, 5, 7]
    
    print(access_list_elements(sample_list, sample_indices_1))
    print(access_list_elements(sample_list, sample_indices_2))