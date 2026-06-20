def evaluate_statement(statement):
    truth_table = {
        'True': True,
        'False': False
    }
    if statement in truth_table:
        return truth_table[statement]
    else:
        raise ValueError(f"Invalid statement: {statement}")

if __name__ == '__main__':
    print(evaluate_statement('True'))
    print(evaluate_statement('False'))