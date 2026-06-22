import operator

CONDITION_CONFIG = {
    "true_true": (True, True),
    "true_false": (True, False),
    "false_true": (False, True),
    "false_false": (False, False),
}

def compare_boolean_sets(x, y, z):
    val1 = x and y or z
    val2 = (x and y) or z
    val3 = x and (y or z)
    val4 = operator.or_(operator.and_(x, y), z)
    val5 = operator.or_(x, operator.and_(y, z))
    return [val1, val2, val3, val4, val5]

def run_demonstration():
    results = []
    for key, (a, b) in CONDITION_CONFIG.items():
        c = True
        values = compare_boolean_sets(a, b, c)
        results.append({
            "input": (a, b, c),
            "a_and_b_or_c": values[0],
            "(a_and_b)_or_c": values[1],
            "a_and_(b_or_c)": values[2],
            "or_and": values[3],
            "or_and_2": values[4]
        })
    return results

if __name__ == '__main__':
    data = run_demonstration()
    for item in data:
        print(item)