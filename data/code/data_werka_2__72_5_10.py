def generate_comparisons(first_list, second_list):
    length = min(len(first_list), len(second_list))
    index = 0
    while index < length:
        value_left = first_list[index]
        value_right = second_list[index]
        if value_left > value_right:
            result = 'A > B'
        elif value_left < value_right:
            result = 'A < B'
        else:
            result = 'A == B'
        yield result
        index += 1

if __name__ == '__main__':
    sample_x = [10, 20, 30, 40]
    sample_y = [10, 15, 35, 45, 50]
    comparison_results = list(generate_comparisons(sample_x, sample_y))
    print(comparison_results)