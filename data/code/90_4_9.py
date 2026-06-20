def check_or_conditions(conditions):
    return [a or b for a, b in conditions]

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False), (True, True)]
    print(check_or_conditions(sample_conditions))