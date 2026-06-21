def contains_zero(numbers):
    for number in numbers:
        if number == 0:
            return True
    return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(contains_zero(sample_list))
    another_sample_list = [-3, -2, -1, 0, 1]
    print(contains_zero(another_sample_list))