import itertools
def check_mutual_exclusivity(conditions, mapping):
    for cond1, cond2 in itertools.combinations(conditions, 2):
        set1 = mapping.get(cond1, set())
        set2 = mapping.get(cond2, set())
        if not set1.isdisjoint(set2):
            if not set1.isdisjoint(set2):
                print(f"Violation found: Conditions '{cond1}' and '{cond2}' imply the same item.")
                print(f"Shared items: {set1.intersection(set2)}")
                return True
    return False
if __name__ == '__main__':
    conditions = ['A is true', 'B is true', 'C is true']
    mapping = {
        'A is true': {'item1', 'item2'},
        'B is true': {'item2', 'item3'},
        'C is true': {'item3', 'item4'}
    }
    print("Checking for mutual exclusivity violations:")
    if check_mutual_exclusivity(conditions, mapping):
        print("Mutual exclusivity violated.")
    else:
        print("No mutual exclusivity violations found.")