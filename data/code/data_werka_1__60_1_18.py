def get_last_item(data):
    if not data:
        return None
    return data[-1]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    EMPTY_LIST = []
    SINGLE_ITEM_LIST = [99]
    
    print(get_last_item(SAMPLE_LIST))
    print(get_last_item(EMPTY_LIST))
    print(get_last_item(SINGLE_ITEM_LIST))