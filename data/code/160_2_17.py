def count_items(item_list):
    item_count = {}
    for item in item_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return item_count

if __name__ == '__main__':
    items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_items(items))