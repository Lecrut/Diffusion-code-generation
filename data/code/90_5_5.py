def check_or_conditions(list_of_tuples):
    satisfying_pairs = []
    for pair in list_of_tuples:
        condition1, condition2 = pair
        if condition1 or condition2:
            satisfying_pairs.append(pair)
    return satisfying_pairs
if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False),
        (True, False)
    ]
    result = check_or_conditions(sample_data)
    print(result)