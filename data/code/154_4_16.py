def item_count_pairs(iterable):
    count = 0
    for item in iterable:
        yield item, count
        count += 1

if __name__ == '__main__':
    sample_list = [42, 3.14, 'hello', True]
    pairs_generator = item_count_pairs(sample_list)
    for pair in pairs_generator:
        print(f'Item: {pair[0]}, Count: {pair[1]}')