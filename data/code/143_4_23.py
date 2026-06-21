def evaluate_statement(statement):
    exec(f'result = {statement}')
    return result

def check_contradictions(stmt1, stmt2):
    try:
        eval_stmt1 = evaluate_statement(stmt1)
        eval_stmt2 = evaluate_statement(stmt2)
        return eval_stmt1 != eval_stmt2
    except Exception as e:
        print(f'Error evaluating statement: {e}')
        return False
if __name__ == '__main__':
    sample_string_1 = 'x > 5'
    sample_string_2 = 'y < 10 and z > 20'
    sample_string_3 = 'a > 10 and a < 5'
    sample_string_4 = 'x > 5 and not (x > 5)'
    sample_string_5 = 'p or q'
    print(check_contradictions(sample_string_1, sample_string_2))
    print(check_contradictions(sample_string_3, sample_string_4))
    print(check_contradictions(sample_string_4, sample_string_5))