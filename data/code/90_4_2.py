def check_or_conditions(conditions):
    return [any(condition) for condition in conditions]

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False)]
    print(check_or_conditions(sample_conditions))