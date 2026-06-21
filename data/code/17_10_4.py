def get_last_element(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    result = get_last_element([1, 2, 3])
    print(result)
    
    result_empty = get_last_element([])
    print(result_empty)