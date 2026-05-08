import itertools
def check_mutual_exclusivity(conditions, mapping):
    for combo in itertools.combinations(conditions, 2):
        cond1, cond2 = combo
        set1 = mapping.get(cond1, set())
        set2 = mapping.get(cond2, set())
        if not set1.isdisjoint(set2):
            yield (cond1, cond2, list(set1.intersection(set2)))
if __name__ == '__main__':
    conditions = [
        'A is true',
        'B is true',
        'C is true',
        'D is true'
    ]
    mapping = {
        'A is true': {'item1', 'item2'},
        'B is true': {'item2', 'item3'},
        'C is true': {'item3', 'item4'},
        'D is true': {'item1', 'item4'}
    }
    violations = list(check_mutual_exclusivity(conditions, mapping))
    if violations:
        print("Mutual exclusivity violated:")
        for c1, c2, intersection in violations:
            print(f"Conditions: '{c1}' and '{c2}' imply the same items: {intersection}")
    else:
        print("No mutual exclusivity violations found.")