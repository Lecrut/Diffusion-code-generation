import sympy as sp

def check_contradictions(statement1, statement2):
    symbols = set(sp.symbols(statement1)).union(set(sp.symbols(statement2)))
    assumptions = {symbol: True for symbol in symbols}
    try:
        result1 = sp.simplify(statement1, assumptions=assumptions)
        result2 = sp.simplify(statement2, assumptions=assumptions)
        if result1 == False and result2 == False:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    statement1 = 'x > 0'
    statement2 = 'x < 0'
    result = check_contradictions(statement1, statement2)
    print(result)