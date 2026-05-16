def find_negatives(data):
    for x in data:
        if x < 0:
            yield True
if __name__ == '__main__':
    input_list = [1, -2, 3, -4, 5, -6, 0]
    result_generator = find_negatives(input_list)
    output_list = list(result_generator)
    print(output_list)