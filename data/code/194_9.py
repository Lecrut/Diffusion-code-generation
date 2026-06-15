def process_list(data):
    result = []
    for item in data:
        if item is not None:
            result.append(item * 2)
    return result
if __name__ == '__main__':
    input_list_1 = [1, 2, None, 4, 5]
    output_1 = process_list(input_list_1)
    print(output_1)
    input_list_2 = [10, None, 20, None, 30]
    output_2 = process_list(input_list_2)
    print(output_2)
    input_list_3 = [None, None, None]
    output_3 = process_list(input_list_3)
    print(output_3)
    input_list_4 = []
    output_4 = process_list(input_list_4)
    print(output_4)