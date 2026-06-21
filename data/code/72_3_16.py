def compare_and_print_greater(first_list, second_list):
    category_map = {
        'greater': 'Greater',
        'equal': 'Equal',
        'less': 'Less'
    }
    results = []
    limit = min(len(first_list), len(second_list))
    for idx in range(limit):
        val1 = first_list[idx]
        val2 = second_list[idx]
        if val1 > val2:
            msg = category_map['greater'] + ": " + str(val1) + " > " + str(val2)
            results.append(msg)
            print(msg)
    return results

if __name__ == '__main__':
    sample_first = [20, 10, 30, 5]
    sample_second = [10, 20, 25, 6]
    returned_output = compare_and_print_greater(sample_first, sample_second)
    print(returned_output)