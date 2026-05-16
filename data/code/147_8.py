def reverse_sorted_generator(data):
    n = len(data)
    for i in range(n - 1, -1, -1):
        yield data[i]
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    reversed_data = reverse_sorted_generator(sample_list)
    result = list(reversed_data)
    print(result)