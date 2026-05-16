def check_mutual_exclusivity(conditions, mapping):
    for i in range(len(conditions)):
        for j in range(i + 1, len(conditions)):
            cond1 = conditions[i]
            cond2 = conditions[j]
            set1 = mapping.get(cond1, set())
            set2 = mapping.get(cond2, set())
            if not set1.isdisjoint(set2):
                return True
    return False
if __name__ == '__main__':
    conditions = [
        'A is true',
        'B is true',
        'C is true'
    ]
    mapping = {
        'A is true': {'item1', 'item2'},
        'B is true': {'item2', 'item3'},
        'C is true': {'item1', 'item4'}
    }
    result = check_mutual_exclusivity(conditions, mapping)
    print(result)