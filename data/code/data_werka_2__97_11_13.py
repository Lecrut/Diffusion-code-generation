def build_or_table(combinations):
    OR_LOOKUP = {
        (False, False): False,
        (False, True): True,
        (True, False): True,
        (True, True): True,
    }
    if not isinstance(combinations, (list, tuple)):
        raise TypeError("Input must be a list or tuple of combinations")
    
    table = []
    for combo in combinations:
        if not isinstance(combo, (list, tuple)) or len(combo) != 2:
            raise ValueError("Each combination must contain exactly two boolean values")
        
        a, b = combo
        if not (isinstance(a, bool) and isinstance(b, bool)):
            raise TypeError("Values must be booleans")
            
        result = OR_LOOKUP[(a, b)]
        table.append([a, b, result])
    return table

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    result = build_or_table(inputs)
    print(result)