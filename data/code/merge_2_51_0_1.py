def find_first_element(elements):
    for item in elements:
        return item
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = find_first_element(sample_list)
    print(result)