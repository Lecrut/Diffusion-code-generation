def is_non_decreasing(input_list):

    def validate_input(lst):
        if not all((isinstance(x, int) for x in lst)):
            raise ValueError('All elements must be integers.')

    def generate_pairs(lst):
        for i in range(len(lst) - 1):
            yield (lst[i], lst[i + 1])
    try:
        validate_input(input_list)
        pairs = generate_pairs(input_list)
        return all((x <= y for x, y in pairs))
    except ValueError as e:
        print(e)
        return False
if __name__ == '__main__':
    sample_input_1 = [1, 2, 3, 4, 5]
    result_1 = is_non_decreasing(sample_input_1)
    print(result_1)
    sample_input_2 = [5, 5, 5, 5]
    result_2 = is_non_decreasing(sample_input_2)
    print(result_2)
    sample_input_3 = [1, 3, 2, 4]
    result_3 = is_non_decreasing(sample_input_3)
    print(result_3)
    sample_input_4 = [10, 9, 8, 7]
    result_4 = is_non_decreasing(sample_input_4)
    print(result_4)