def evaluate_statement(statement):
    return eval(statement)

if __name__ == '__main__':
    statements = [
        "2 + 2 == 4",
        "3 * 3 != 9",
        "True or False",
        "False and True",
        "not (1 == 0)"
    ]
    
    for statement in statements:
        print(evaluate_statement(statement))