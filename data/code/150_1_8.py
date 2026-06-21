TARGET_ITEM = 2

def remove_item_from_list(input_list):
    return list(filter(lambda item: item != TARGET_ITEM, input_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 4, 2, 5]
    result = remove_item_from_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Target item: {TARGET_ITEM}")
    print(f"Result list: {result}")