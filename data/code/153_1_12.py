def check_target_presence(data, target):
    data_set = set(data)
    return target in data_set

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    target_value = 35
    print(f"List: {sample_list}, Target: {target_value}, Exists: {check_target_presence(sample_list, target_value)}")
    
    sample_list_2 = ['apple', 'banana', 'cherry']
    target_string = 'grape'
    print(f"List: {sample_list_2}, Target: {target_string}, Exists: {check_target_presence(sample_list_2, target_string)}")