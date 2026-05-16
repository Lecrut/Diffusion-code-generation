def check_or_conditions(list_of_tuples):
    result = []
    for condition_pair in list_of_tuples:
        a, b = condition_pair
        if a or b:
            result.append(condition_pair)
    return result
if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    satisfied_pairs = check_or_conditions(sample_data)
    print(satisfied_pairs)