def list_iterator(input_list):
    for item in input_list:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    iterator = list_iterator(sample_list)
    for number in iterator:
        print(number)