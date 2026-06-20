def evaluate_statement(statement):
    try:
        return eval(statement)
    except Exception as e:
        return False

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
        print(evaluate_statement(statement))