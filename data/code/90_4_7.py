def check_or_conditions(conditions):
    return [condition[0] or condition[1] for condition in conditions]

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False)]
    print(check_or_conditions(sample_conditions))