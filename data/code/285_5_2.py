def find_smaller_than_neighbor_indices(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            yield i
if __name__ == '__main__':
    input_list = [1, 3, 2, 5, 4, 7, 6]
    result_generator = find_smaller_than_neighbor_indices(input_list)
    result_list = list(result_generator)
    print(result_list)