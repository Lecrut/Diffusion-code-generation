def get_middle_item(items):
    length = len(items)
    index = length // 2
    if length % 2 == 0:
        if index > 0:
            return items[index - 1]
    return items[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_middle_item(sample_data))
    sample_data_even = [1, 2, 3, 4]
    print(get_middle_item(sample_data_even))