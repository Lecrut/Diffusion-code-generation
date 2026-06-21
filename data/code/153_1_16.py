def check_target_presence(data, target):
    data_set = set(data)
    return target in data_set

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_fruit = 'orange'
    result = check_target_presence(sample_list, target_fruit)
    print(f"List: {sample_list}, Target: {target_fruit}, Exists: {result}")