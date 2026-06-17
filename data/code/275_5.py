def list_iterator(data):
    for item in data:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    iterator = list_iterator(sample_list)
    result_list = []
    for element in iterator:
        result_list.append(element)
    print(result_list)