def find_first_element(elements):
    for element in elements:
        return element
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = find_first_element(sample_list)
    print(result)