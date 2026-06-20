def evaluate_logical_statement(statement):
    return eval(statement)

if __name__ == '__main__':
    statements = [
        "True",
        "False",
        "not True",
        "not False",
        "True and True",
        "True and False",
        "False and True",
        "False and False",
        "True or True",
        "True or False",
        "False or True",
        "False or False"
    ]
    
    for statement in statements:
        print(f"Statement: {statement}, Truth Value: {evaluate_logical_statement(statement)}")