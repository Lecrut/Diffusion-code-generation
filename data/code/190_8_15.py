def substring_exists(data_list, sub):
    return any(sub in element for element in data_list)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    sub1 = 'an'
    sub2 = 'berry'
    print(f"Checking if '{sub1}' exists in {sample_list}: {substring_exists(sample_list, sub1)}")
    print(f"Checking if '{sub2}' exists in {sample_list}: {substring_exists(sample_list, sub2)}")