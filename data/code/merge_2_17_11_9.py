def check_item_presence(iterable_data: any, target) -> bool:
    try:
        if not hasattr(iterable_data, '__iter__'):
            raise TypeError("Input must be an iterable.")
        for item in iterable_data:
            if item == target:
                return True
        return False
    except Exception as e:
        print(f"An error occurred during iteration: {e}")
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'apple', 4]
    sample_tuple = (5, 6, 'banana')
    sample_set = {'orange', 'pear'}
    target_to_find = 'apple'
    result_list = check_item_presence(sample_list, target_to_find)
    print(f"Found in list: {result_list}")
    if isinstance(result_list, bool):
        found_in_tuple = check_item_presence(sample_tuple, target_to_find)
        print(f"Found in tuple: {found_in_tuple}")
        found_in_set = check_item_presence(sample_set, 'orange')
        print(f"Found in set: {found_in_set}")