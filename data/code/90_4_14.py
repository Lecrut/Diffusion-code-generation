def check_or_conditions(conditions):
    if not all(isinstance(condition, tuple) and len(condition) == 2 for condition in conditions):
        raise ValueError("Each item must be a tuple of two boolean values")
    return [any(condition) for condition in conditions]

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False)]
    print(check_or_conditions(sample_conditions))