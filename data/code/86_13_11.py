def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    TRUE = True
    FALSE = False
    
    results = {
        (TRUE, TRUE): TRUE,
        (FALSE, FALSE): TRUE,
        (TRUE, FALSE): FALSE
    }
    
    for inputs, expected in results.items():
        result = compare_booleans(*inputs)
        print(f"compare_booleans{inputs} -> {result}, Expected: {expected}")