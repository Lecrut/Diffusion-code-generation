def evaluate_equality(a: any, b: any) -> bool:
    return a is None and b is None or a == b
if __name__ == '__main__':
    print(evaluate_equality(None, None))        
    print(evaluate_equality(5, 5))              
    print(evaluate_equality("a", "b"))           
    print(evaluate_equality(None, 10))