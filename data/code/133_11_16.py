import ast

def evaluate_statement(statement):
    try:
        return bool(ast.literal_eval(statement))
    except (ValueError, SyntaxError):
        raise ValueError("Invalid logical statement")

if __name__ == '__main__':
    sample_statements = [
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
        "False or False",
        "1 == 1",
        "1 != 2",
        "3 > 2",
        "3 < 2"
    ]
    
    for statement in sample_statements:
        print(f"{statement}: {evaluate_statement(statement)}")