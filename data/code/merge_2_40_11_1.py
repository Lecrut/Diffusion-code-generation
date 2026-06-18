def safe_contains(data: dict, key) -> bool:
    try:
        return key in data
    except TypeError:
        return False
if __name__ == '__main__':
    sample_dict = {'apple': 10, 'banana': 20}
    result1 = safe_contains(sample_dict, 'apple')
    result2 = safe_contains(sample_dict, 'orange')
    int_key_result = safe_contains(sample_dict, 42)
    print(result1)
    print(result2)
    print(int_key_result)