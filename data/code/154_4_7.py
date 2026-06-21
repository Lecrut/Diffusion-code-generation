ITEM_COUNT_START = 0

def item_count_pairs(iterable):
    count = ITEM_COUNT_START
    for item in iterable:
        yield item, count
        count += 1

if __name__ == '__main__':
    sample_list = [42, 3.14, 'hello', True]
    for item, count in item_count_pairs(sample_list):
        print(f'Item: {item}, Count: {count}')