def find_negatives(data):
    for item in data:
        if item < 0:
            yield True
if __name__ == '__main__':
    sample_list = [1, -2, 3, -4, 5, -6, 0]
    result_generator = find_negatives(sample_list)
    output_list = list(result_generator)
    print(output_list)