def list_to_set(lst):
    return set(lst)

def item_exists(data, target):
    data_set = list_to_set(data)
    return target in data_set

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(f"List: {sample_list}, Target: {target_value}, Exists: {item_exists(sample_list, target_value)}")