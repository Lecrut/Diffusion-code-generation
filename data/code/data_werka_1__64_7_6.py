def index_generator(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    try:
        return next(index_generator(reversed(data), item))
    except StopIteration:
        return -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 30, 60, 30]
    target_item = 30
    final_index = find_final_index(sample_data, target_item)
    print(final_index)