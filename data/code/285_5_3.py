def find_smaller_than_neighbor_indices(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            yield i
if __name__ == '__main__':
    input_list = [10, 5, 8, 3, 9, 1]
    result_generator = find_smaller_than_neighbor_indices(input_list)
    result_list = list(result_generator)
    print(result_list)