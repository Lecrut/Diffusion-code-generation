def list_to_set(data):
    return set(data)

def item_exists(data, target):
    data_set = list_to_set(data)
    return target in data_set

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_string = 'banana'
    print(f"List: {sample_list}, Target: {target_string}, Exists: {item_exists(sample_list, target_string)}")