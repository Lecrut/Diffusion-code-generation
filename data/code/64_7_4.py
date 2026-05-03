def index_generator(data, item):
    for index, element in enumerate(data):
        if element == item:
            yield index
if __name__ == '__main__':
    sample_data = [1, 5, 2, 5, 8, 5, 3]
    target_item = 5
    indices = list(index_generator(sample_data, target_item))
    print(f"Indices of {target_item}: {indices}")
    final_index = -1
    if indices:
        final_index = indices[-1]
    print(f"Final index of {target_item}: {final_index}")