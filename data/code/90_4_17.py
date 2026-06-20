OR_CONDITION = lambda p1, p2: p1 or p2

def check_or_conditions(conditions):
    return [OR_CONDITION(*condition) for condition in conditions]

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False)]
    print(check_or_conditions(sample_conditions))