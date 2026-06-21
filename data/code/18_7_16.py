def get_middle_item(data):
    if not data:
        return None
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_list)
    print(result)