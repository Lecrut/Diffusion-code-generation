import itertools

def truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([True, False], repeat=3))
    results = []

    for combo in combinations:
        A, B, C = combo
        result = (A and B) or not C
        results.append((combo + (result,)))

    return results

if __name__ == '__main__':
    print(truth_table())