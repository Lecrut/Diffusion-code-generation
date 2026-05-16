def check_or_relationship(list_of_tuples):
    results = []
    for pair in list_of_tuples:
        condition1, condition2 = pair
        if condition1 or condition2:
            results.append(True)
        else:
            results.append(False)
    return results
if __name__ == '__main__':
    sample_data = [
        (True, False),
        (False, False),
        (True, True),
        (False, True),
        (False, False)
    ]
    output = check_or_relationship(sample_data)
    print(output)