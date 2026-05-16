def reverse_sorted_generator(input_list):
    n = len(input_list)
    for i in range(n - 1, -1, -1):
        yield input_list[i]
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    reversed_generator = reverse_sorted_generator(sample_list)
    result = list(reversed_generator)
    print(result)