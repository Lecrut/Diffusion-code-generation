def count_items(input_dict):
    item_count = {}
    for key, value in input_dict.items():
        if value in item_count:
            item_count[value] += 1
        else:
            item_count[value] = 1
    return item_count

if __name__ == '__main__':
    sample_dict = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable', 'apple': 'fruit'}
    print(count_items(sample_dict))