def contains_zero(numbers):
    zero_found = False
    for number in numbers:
        if number == 0:
            zero_found = True
            break
    return zero_found

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(contains_zero(sample_list))
    another_sample_list = [-5, -10, 0, 5]
    print(contains_zero(another_sample_list))