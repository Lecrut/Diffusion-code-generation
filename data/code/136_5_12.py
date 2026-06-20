def evaluate_expression():
    values = {
        "a": True,
        "b": False,
        "c": True,
        "d": False
    }
    
    result = (values["a"] and not values["b"]) or (values["c"] and not values["d"])
    return result

if __name__ == '__main__':
    print(evaluate_expression())