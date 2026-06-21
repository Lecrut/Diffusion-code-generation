SAMPLE_LIST = [1, 5, 2, 8, 3]
TARGET_ITEM = 2

def check_item_exists(data_list, target):
    return target in data_list

if __name__ == '__main__':
    result = check_item_exists(SAMPLE_LIST, TARGET_ITEM)
    print(f"Does {TARGET_ITEM} exist in the list? {result}")