def check_substring_in_list(data_list, substring):
    if not all(isinstance(item, str) for item in data_list):
        raise ValueError("All elements in the list must be strings")
    return any(substring in item for item in data_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    substring1 = 'an'
    print(f"Checking if '{substring1}' is in {sample_list}: {check_substring_in_list(sample_list, substring1)}")
    
    sample_list2 = ['hello', 'world', 'python']
    substring2 = 'xyz'
    print(f"Checking if '{substring2}' is in {sample_list2}: {check_substring_in_list(sample_list2, substring2)}")