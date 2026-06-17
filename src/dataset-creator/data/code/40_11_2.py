def verify_key_in_dict(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_str = verify_key_in_dict(sample_data, 'apple')
    try:
        result_int = verify_key_in_dict(sample_data, 100)
    except Exception as e:
        print(f"Error occurred for integer check: {e}")
    sample_data_with_tuple = {'(a,b)': 'value'}
    result_tuple = verify_key_in_dict(sample_data_with_tuple, ('a', 'b'))
    print(result_str)