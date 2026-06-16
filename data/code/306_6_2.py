def list_iterator(input_list):
    for item in input_list:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Starting iteration:")
    for number in list_iterator(sample_list):
        print(number)
    print("Iteration finished.")