def check_any_condition(sequence, condition):
    found = False
    for element in sequence:
        if condition(element):
            found = True
            break
    return found

if __name__ == '__main__':
    data_points = [None, False, 0, '', [], {}, 42]
    predicate_func = lambda val: val is not None and val is not False and val != 0 and val != '' and val != [] and val != {}
    outcome = check_any_condition(data_points, predicate_func)
    print(outcome)