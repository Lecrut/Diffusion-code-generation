def count_items(iterable):
    try:
        iterator = iter(iterable)
        index = 0
        while True:
            item = next(iterator)
            yield (index, item)
            index += 1
    except StopIteration:
        pass
def count_items_v2(iterable):
    try:
        return list(range(len(list(iterable)))) + [(len(list(iterable)), None)] if len(list(iterable)) > 0 else [None]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    try:
        result_list = list(range(len(sample_data))) + [None] if len(sample_data) > 0 else []
        for idx, item in enumerate(result_list):
            print(f"Index {idx}: Item is None")
        count = sum(1 for _ in sample_data)
        print(f"Total items counted: {count}")
    except Exception as e:
        pass