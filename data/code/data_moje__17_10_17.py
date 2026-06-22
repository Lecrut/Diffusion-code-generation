def get_last_element(items):
    if not items:
        return None
    return items[len(items) - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_element(sample_list)
    print(result)
    
    empty_list = []
    empty_result = get_last_element(empty_list)
    print(empty_result)