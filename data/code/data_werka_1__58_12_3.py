def safe_first_element(iterable):
    try:
        return iterable[0]
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_string = "hello"
    sample_dict = {'a': 1, 'b': 2}
    sample_set = {7, 8, 9}
    sample_empty_list = []
    
    print(safe_first_element(sample_list))
    print(safe_first_element(sample_tuple))
    print(safe_first_element(sample_string))
    print(safe_first_element(sample_dict))  # This will print None
    print(safe_first_element(sample_set))   # This will print None
    print(safe_first_element(sample_empty_list))