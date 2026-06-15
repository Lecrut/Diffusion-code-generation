def list_iterator(input_list):
    for item in input_list:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    generator = list_iterator(sample_list)
    result_list = []
    for element in generator:
        result_list.append(element)
    print(result_list)