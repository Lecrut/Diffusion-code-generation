def item_exists(data, target):
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        raise ValueError("Data must be a list of strings")
    return target in set(data)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_string = 'banana'
    print(f"List: {sample_list}, Target: '{target_string}', Exists: {item_exists(sample_list, target_string)}")