def evaluate_conditions(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    conditions = {
        'A': True,
        'B': False
    }
    result = evaluate_conditions(conditions['A'], conditions['B'])
    print(f'AND Result: {result}')