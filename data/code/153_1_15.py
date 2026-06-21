TARGET_NOT_FOUND = False

def item_exists(data, target):
    return target in set(data)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(f"List: {sample_list}, Target: {target_value}, Exists: {item_exists(sample_list, target_value)}")
    
    sample_list = ['apple', 'banana', 'cherry']
    target_value = 'banana'
    print(f"List: {sample_list}, Target: {target_value}, Exists: {item_exists(sample_list, target_value)}")
    
    sample_list = []
    target_value = 5
    print(f"List: {sample_list}, Target: {target_value}, Exists: {item_exists(sample_list, target_value)}")