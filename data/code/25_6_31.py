def contains_zero(numbers):
    return 0 in numbers

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = contains_zero(sample_list)
    print(result)

    another_sample_list = [10, 20, 30, 40, 50, 0]
    result = contains_zero(another_sample_list)
    print(result)