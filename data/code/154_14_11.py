def tally_items(items):
    count_dict = {}
    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return dict(sorted(count_dict.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(tally_items(sample_items))