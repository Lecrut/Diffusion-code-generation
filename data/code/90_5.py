def check_or_conditions(list_of_tuples):
    satisfied_pairs = []
    for condition_pair in list_of_tuples:
        if condition_pair[0] or condition_pair[1]:
            satisfied_pairs.append(condition_pair)
    return satisfied_pairs
if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    result = check_or_conditions(sample_data)
    print(result)