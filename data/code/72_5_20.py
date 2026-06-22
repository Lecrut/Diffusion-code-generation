def compare_pairs(list_a, list_b):
    length = min(len(list_a), len(list_b))
    index = 0
    while index < length:
        value_a = list_a[index]
        value_b = list_b[index]
        index += 1
        if value_a > value_b:
            yield 'A > B'
        elif value_a < value_b:
            yield 'A < B'
        else:
            yield 'A == B'

if __name__ == '__main__':
    first_list = [10, 20, 30, 40]
    second_list = [10, 15, 35, 40, 50]
    comparison_results = list(compare_pairs(first_list, second_list))
    print(comparison_results)