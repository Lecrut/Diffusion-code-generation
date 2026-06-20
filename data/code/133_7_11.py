def evaluate_relation(expression):
    if expression == '1':
        return True
    elif expression == '0':
        return False
    else:
        raise ValueError("Invalid relational expression encountered")

if __name__ == '__main__':
    expressions = ['1', '0', '1', '0']
    results = [evaluate_relation(expr) for expr in expressions]
    print(results)