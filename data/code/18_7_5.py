def get_middle_item(items):
    length = len(items)
    index = length // 2
    return items[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_data)
    print(result)