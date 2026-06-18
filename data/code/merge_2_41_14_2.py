import sys
def count_elements(container):
    if isinstance(container, (list, tuple)):
        return len(container)
    elif isinstance(container, dict):
        return len(container.keys())
    elif hasattr(container, '__iter__') and not isinstance(container, str):
        try:
            iterator = iter(container)
            count = 0
            while True:
                next(iterator)
                count += 1
            return count - 1 if container else 0
        except StopIteration:
            return len(list(container))
    elif isinstance(container, set):
        return len(container)
    else:
        try:
            items = list(container)
            return len(items)
        except TypeError:
            return None
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b')
    sample_dict = {'key1': 'val1'}
    sample_set = {10, 20}
    results = []
    for item in [sample_list, sample_tuple, sample_dict, sample_set]:
        count = count_elements(item)
        if isinstance(count, int):
            print(f"Container type: {type(item).__name__}, Element count: {count}")