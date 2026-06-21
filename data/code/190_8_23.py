def check_substring_presence(data_list, substring):
    return any(substring in element for element in data_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    substring1 = 'an'
    substring2 = 'grape'

    print(f"Checking if '{substring1}' is present in {sample_list}: {check_substring_presence(sample_list, substring1)}")
    print(f"Checking if '{substring2}' is present in {sample_list}: {check_substring_presence(sample_list, substring2)}")