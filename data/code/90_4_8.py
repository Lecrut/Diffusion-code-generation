def check_or_conditions(conditions):
    results = []
    for condition in conditions:
        if isinstance(condition, tuple) and len(condition) == 2 and all(isinstance(x, bool) for x in condition):
            result = condition[0] or condition[1]
            results.append(result)
        else:
            raise ValueError("Each item must be a tuple of two boolean values")
    return results

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False)]
    print(check_or_conditions(sample_conditions))