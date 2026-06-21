def check_target_presence(data, target):
    return target in set(data)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(f"List: {sample_list}, Target: {target_value}, Exists: {check_target_presence(sample_list, target_value)}")