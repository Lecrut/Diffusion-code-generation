def exclude_element(collection, target):
    return [item for item in collection if item != target]

if __name__ == '__main__':
    sample_data = ['a', 'b', 'c', 'd', 'c', 'e']
    unwanted_item = 'c'
    refined_list = exclude_element(sample_data, unwanted_item)
    print(refined_list)