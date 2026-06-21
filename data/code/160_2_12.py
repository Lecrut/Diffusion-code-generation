ITEM_COUNT = {}

def update_frequency(item_name):
    if item_name in ITEM_COUNT:
        ITEM_COUNT[item_name] += 1
    else:
        ITEM_COUNT[item_name] = 1

def get_frequencies(item_list):
    for item in item_list:
        update_frequency(item)
    return ITEM_COUNT

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(get_frequencies(sample_items))