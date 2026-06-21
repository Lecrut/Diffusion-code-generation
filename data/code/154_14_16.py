def tally_items(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    item_count = {}
    for item in sequence:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    return dict(sorted(item_count.items(), key=lambda x: x[0]))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(f"Tally of items in {sample_list}: {tally_items(sample_list)}")