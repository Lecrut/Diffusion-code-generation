def find_smaller_indices(data):
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            yield i
if __name__ == '__main__':
    input_list = [5, 2, 8, 1, 9, 3]
    result_generator = find_smaller_indices(input_list)
    result_list = list(result_generator)
    print(result_list)