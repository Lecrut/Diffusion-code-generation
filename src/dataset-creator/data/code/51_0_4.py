def find_first_element(data):
    for item in data:
        return item
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = find_first_element(sample_list)
    print(result)