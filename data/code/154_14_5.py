def tally_items(item_list):
    item_count = {}
    for item in item_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return dict(sorted(item_count.items()))

if __name__ == '__main__':
    sample_values = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(tally_items(sample_values))