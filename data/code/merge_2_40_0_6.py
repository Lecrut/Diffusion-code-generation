def check_key_in_dict(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_data = {"apple": 10, "banana": 20, "cherry": 30}
    target_key = "banana"
    if check_key_in_dict(sample_data, target_key):
        print(f"The key '{target_key}' exists in the dictionary.")
    else:
        print(f"The key '{target_key}' does not exist in the dictionary.")