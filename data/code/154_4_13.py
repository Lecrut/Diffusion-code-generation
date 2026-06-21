def item_count_pairs(iterable):
    count = 0
    for item in iterable:
        yield item, count
        count += 1

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z']
    for item, count in item_count_pairs(sample_list):
        print(f'Item: {item}, Count: {count}')