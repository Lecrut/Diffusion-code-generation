def list_to_generator(input_list):
    for item in input_list:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    generator = list_to_generator(sample_list)
    for item in generator:
        print(item)