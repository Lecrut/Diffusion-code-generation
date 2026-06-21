def get_middle_value(items):
    if not items:
        raise ValueError("List must not be empty")
    length = len(items)
    if length % 2 == 0:
        raise ValueError("List must have an odd number of elements to have a single middle value")
    middle_index = length // 2
    return items[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_list)
    print(result)