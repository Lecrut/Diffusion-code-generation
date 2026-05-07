def check_or_conditions(list_of_tuples):
    results = []
    for conditions in list_of_tuples:
        if conditions[0] or conditions[1]:
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
    output = check_or_conditions(sample_data)
    print(output)