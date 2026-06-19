def find_all_indices(data, item):
    for i, x in enumerate(data):
        if x == item:
            yield i

def find_final_index(data, item):
    indices = list(find_all_indices(data, item))
    return indices[-1] if indices else -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_item = 50
    final_index = find_final_index(sample_data, target_item)
    print(final_index)