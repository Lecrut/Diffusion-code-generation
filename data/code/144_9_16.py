def biconditional(a: bool, b: bool) -> bool:
    return a == b

def generate_truth_table(n: int) -> list[list[bool]]:
    truth_table = [[biconditional(a, b) for b in [False, True]] for a in [False, True]]
    return truth_table

if __name__ == '__main__':
    sample_values = (True, False)
    truth_table_data = generate_truth_table(len(sample_values))
    print(truth_table_data)