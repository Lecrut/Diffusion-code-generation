def contains_zero(numbers):
    for number in numbers:
        if number == 0:
            return True
    return False

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    zero_exists = contains_zero(sample_list)
    print(zero_exists)

    another_sample_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    print(contains_zero(another_sample_list))