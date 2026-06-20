def is_valid_statement(statement):
    return statement.lower() in {'true', 'false'}

def evaluate_logical_statement(statement):
    if not is_valid_statement(statement):
        raise ValueError(f"Invalid logical statement: {statement}")
    
    return eval(statement)

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
        "False or False"
    ]
    
    results = [evaluate_logical_statement(statement) for statement in sample_statements]
    print(results)