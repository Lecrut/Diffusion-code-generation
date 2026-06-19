def consecutive_diff_generator(numbers):
    for i in range(1, len(numbers)):
        yield abs(numbers[i] - numbers[i - 1])

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 4]
    diff_gen = consecutive_diff_generator(sample_list)
    for diff in diff_gen:
        print(diff)