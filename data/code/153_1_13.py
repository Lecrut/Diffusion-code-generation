def target_exists(lst, target):
    return target in set(lst)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_item = 'banana'
    print(f"List: {sample_list}, Target: {target_item}, Exists: {target_exists(sample_list, target_item)}")