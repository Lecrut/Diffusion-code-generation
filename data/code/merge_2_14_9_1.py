import sys
def remove_duplicates_optimized(data):
    seen = set()
    result = []
    for item in data:
        if isinstance(item, (list, tuple)):
            try:
                key = id(item)
            except TypeError:
                continue
        elif not seen.add(item):
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', (4, 5), ('6', 7), 8, 9] * 10 + ['extra']
    cleaned_list = remove_duplicates_optimized(sample_data)
    print(cleaned_list)