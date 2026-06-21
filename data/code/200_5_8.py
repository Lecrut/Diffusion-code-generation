def find_max_index(numbers):
    return max(enumerate(numbers), key=lambda x: x[1])[0]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(find_max_index(sample_list))