def get_middle_item(data):
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_list)
    print(result)