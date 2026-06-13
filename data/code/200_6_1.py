def list_iterator(input_list):
    for item in input_list:
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    generator = list_iterator(data)
    result_list = []
    for element in generator:
        result_list.append(element)
    print(result_list)