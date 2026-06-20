def evaluate_logical_statements():
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
    
    results = [eval(statement) for statement in statements]
    
    return results

if __name__ == '__main__':
    print(evaluate_logical_statements())