def substring_exists_in_list(data_list, substring):
    if not all(isinstance(element, str) for element in data_list):
        raise ValueError("All elements in the list must be strings")
    return any(substring in element for element in data_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    substring_present = 'an'
    substring_absent = 'grape'
    
    print(f"Checking if '{substring_present}' exists in {sample_list}: {substring_exists_in_list(sample_list, substring_present)}")
    print(f"Checking if '{substring_absent}' exists in {sample_list}: {substring_exists_in_list(sample_list, substring_absent)}")