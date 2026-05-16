def check_or_conditions(list_of_tuples):
    satisfying_pairs = []
    for condition_pair in list_of_tuples:
        if condition_pair[0] or condition_pair[1]:
            satisfying_pairs.append(condition_pair)
    return satisfying_pairs
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