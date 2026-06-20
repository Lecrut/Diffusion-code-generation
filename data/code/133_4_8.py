def evaluate_statement(statement):
    return eval(statement)

if __name__ == '__main__':
    print(evaluate_statement('True'))
    print(evaluate_statement('False'))
    print(evaluate_statement('2 + 2 == 4'))
    print(evaluate_statement('3 > 5'))