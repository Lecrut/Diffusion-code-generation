def item_count_pairs(large_list):
    for index, item in enumerate(large_list):
        yield (item, index + 1)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    for item, count in item_count_pairs(sample_list):
        print(f'Item: {item}, Count: {count}')