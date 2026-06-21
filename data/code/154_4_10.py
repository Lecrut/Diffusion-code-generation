def item_count_pairs(iterable):
    count = 0
    for item in iterable:
        yield item, count
        count += 1

def validate_iterable(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    validate_iterable(sample_list)
    for item, count in item_count_pairs(sample_list):
        print(f'Item: {item}, Count: {count}')