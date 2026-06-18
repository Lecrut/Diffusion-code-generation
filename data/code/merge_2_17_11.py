def check_item_presence(iterable_data: any, target) -> bool:
    try:
        if not hasattr(iterable_data, '__iter__'):
            raise TypeError("Input must be an iterable data structure.")
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
    target_item = 'apple'
    result_list = check_item_presence(sample_list, target_item)
    print(f"List contains '{target_item}': {result_list}")
    target_item_2 = 100
    result_tuple = check_item_presence(sample_tuple, target_item_2)
    print(f"Tuple contains {target_item_2}: {result_tuple}")