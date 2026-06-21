ITEM_NAME_SET = set()

def unique_items(items):
    global ITEM_NAME_SET
    result = []
    for item in items:
        if item not in ITEM_NAME_SET:
            ITEM_NAME_SET.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(unique_items(sample_items))