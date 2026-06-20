import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    truth_values = list(itertools.product([False, True], repeat=3))
    truth_table = {combo: (a or b and not c) for a, b, c in truth_values}
    return truth_table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table()
    print("Truth Table")
    print("-----------")
    for combo, result in sorted(sample_truth_table.items()):
        A, B, C = combo
        print(f"A: {A}, B: {B}, C: {C} -> Result: {result}")