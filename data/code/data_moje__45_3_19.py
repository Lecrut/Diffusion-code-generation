def find_minimum(numbers):
    return min([x for x in numbers])

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_minimum(sample_list))