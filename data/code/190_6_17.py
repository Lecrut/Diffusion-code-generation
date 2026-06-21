KEY_CHECK_SET = set()

def is_key_present(key_list, target_key):
    global KEY_CHECK_SET
    if not KEY_CHECK_SET:
        KEY_CHECK_SET.update(key_list)
    return target_key in KEY_CHECK_SET

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    key_to_check = 'banana'
    result1 = is_key_present(sample_list, key_to_check)
    print(f"Key: {key_to_check}, Present: {result1}")

    key_to_check = 'grape'
    result2 = is_key_present(sample_list, key_to_check)
    print(f"Key: {key_to_check}, Present: {result2}")