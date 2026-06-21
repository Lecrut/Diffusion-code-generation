def tally_items(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    tally = {}
    for item in sequence:
        tally[item] = tally.get(item, 0) + 1
    
    return dict(sorted(tally.items()))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(f"Tally of items in {sample_list}: {tally_items(sample_list)}")