def find_max_index(numbers):
    return numbers.index(max(numbers))

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(find_max_index(sample_list))