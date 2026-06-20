# Named constant for logical statements
LOGICAL_STATEMENTS = [
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

def evaluate_statement(statement):
    return eval(statement, {"__builtins__": None}, {"True": True, "False": False})

if __name__ == '__main__':
    results = [evaluate_statement(stmt) for stmt in LOGICAL_STATEMENTS]
    print(results)