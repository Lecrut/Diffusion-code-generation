def evaluate_nested_logic(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = {
        'a': True,
        'b': False,
        'c': False,
        'd': True
    }
    
    result = evaluate_nested_logic(**sample_values)
    print(result)