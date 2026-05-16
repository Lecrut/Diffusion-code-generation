import itertools
def evaluate_conditions(conditions, values):
    results = []
    for cond, val in zip(conditions, values):
        if cond:
            results.append(val)
        else:
            results.append(None)
    return results
def check_consistency(if_statements, initial_values):
    all_statements = []
    for statement in if_statements:
        if statement['condition']:
            all_statements.append(statement['consequence'])
        else:
            all_statements.append(None)
    results = []
    for statement in all_statements:
        if statement is not None:
            results.append(statement)
        else:
            results.append(None)
    return results
def assess_logical_consistency(if_statements, initial_values):
    inconsistent_sets = set()
    for statement in if_statements:
        condition = statement['condition']
        consequence = statement['consequence']
        if condition:
            result = consequence
        else:
            result = None
        if result is not None:
            if result not in initial_values:
                inconsistent_sets.add(f"Contradiction: {result} derived from condition {condition}")
            for other_statement in if_statements:
                if other_statement is not statement:
                    other_condition = other_statement['condition']
                    other_consequence = other_statement['consequence']
                    if other_condition:
                        other_result = other_consequence
                    else:
                        other_result = None
                    if other_result is not None and result != other_result:
                        inconsistent_sets.add(f"Contradiction between {statement} and {other_statement}: {result} vs {other_result}")
    return list(inconsistent_sets)
if __name__ == '__main__':
    sample_if_statements = [
        {'condition': True, 'consequence': 10},
        {'condition': False, 'consequence': 20},
        {'condition': True, 'consequence': 10},
        {'condition': False, 'consequence': 30},
        {'condition': True, 'consequence': 20}
    ]
    initial_values = {
        'True': 1,
        'False': 0
    }
    inconsistencies = assess_logical_consistency(sample_if_statements, initial_values)
    print("Inconsistencies Found:")
    if inconsistencies:
        for inc in inconsistencies:
            print(inc)
    else:
        print("No logical inconsistencies found.")