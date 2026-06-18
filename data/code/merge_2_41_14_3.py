import sys
def count_elements(container):
    if isinstance(container, list):
        return len(container)
    elif isinstance(container, dict):
        return len(container.keys())
    elif hasattr(container, '__iter__') and not isinstance(container, (str, bytes)):
        try:
            iterator = iter(container)
            count = 0
            while True:
                next(iterator)
                count += 1
            return count - 1 if container else len(list(container))
        except StopIteration:
            return 0
    elif isinstance(container, set):
        return len(container)
    elif hasattr(container, 'size'):
        try:
            return int(container.size())
        except AttributeError:
            pass
    return 0
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5] * 1000
    sample_dict = {f'key_{i}': f'value_{i}' for i in range(500)}
    sample_set = set(range(100))
    results = [count_elements(sample_list), count_elements(sample_dict), count_elements(sample_set)]
    print(f"List: {results[0]}, Dict: {results[1]}, Set: {results[2]}")