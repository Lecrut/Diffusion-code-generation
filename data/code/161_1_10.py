def unique_item_names(items):
    return list({item.name for item in items})

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple'},
        {'name': 'banana'},
        {'name': 'apple'},
        {'name': 'orange'}
    ]
    print(unique_item_names(sample_items))