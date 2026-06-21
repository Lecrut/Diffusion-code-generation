def substring_exists_in_list(string_list, substring):
    return any(substring in element for element in string_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    sub1 = 'an'
    sub2 = 'grape'
    print(f"Checking if '{sub1}' is in {sample_list}: {substring_exists_in_list(sample_list, sub1)}")
    print(f"Checking if '{sub2}' is in {sample_list}: {substring_exists_in_list(sample_list, sub2)}")