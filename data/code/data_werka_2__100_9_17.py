def is_valid_boolean_expression(expr: str) -> bool:
    try:
        compile(expr, '<string>', 'eval')
    except SyntaxError:
        return False
    except Exception:
        return False
    
    allowed_names = {
        'True': True,
        'False': False,
        'true': True,
        'false': False,
        'TRUE': True,
        'FALSE': False,
        'None': None,
    }
    
    try:
        result = eval(expr, {"__builtins__": {}}, allowed_names)
    except NameError:
        return False
    except Exception:
        return False
        
    if isinstance(result, bool):
        return True
        
    return False

if __name__ == '__main__':
    samples = [
        "True and False",
        "1 == 1",
        "True or False",
        "not True",
        "True and",
        "if True",
        "1 + 1",
        "True",
        "False",
        "True == True",
        "1 > 0",
        "x and y",
        "True and True",
        "False or True",
        "not False",
        "True and not False",
        "True or 1",
        "1 and True",
        "True and 1",
        "True or 0",
        "0 or True",
        "True and 0",
        "0 and True",
        "True and None",
        "None and True",
        "True or None",
        "None or True",
        "True and True",
        "False and False",
        "True or False",
        "False or False",
        "not True",
        "not False",
        "not not True",
        "not not False",
        "True and True and True",
        "False or False or False",
        "True and False or True",
        "True or False and False",
        "(True and False) or True",
        "True and (False or True)",
        "True == True",
        "False == False",
        "True == False",
        "True != False",
        "True is True",
        "True is False",
        "True in [True]",
        "True in [False]",
        "True not in [False]",
        "True not in [True]",
        "True and True",
        "True or True",
        "False and False",
        "False or False",
        "not True",
        "not False",
        "True and True",
        "True or True",
        "False and False",
        "False or False",
        "not True",
        "not False",
        "True and True",
        "True or True",
        "False and False",
        "False or False",
        "not True",
        "not False",
    ]
    
    results = [is_valid_boolean_expression(s) for s in samples]
    print(results)