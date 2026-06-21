def contains_zero(numbers):
    return 0 in numbers
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(contains_zero(sample_list))
    another_sample_list = [0, 1, 2, 3, 4]
    print(contains_zero(another_sample_list))