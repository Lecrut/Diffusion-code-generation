def evaluate_equality(input_a: any, input_b: any) -> bool:
    return input_a is None and input_b is None or input_a == input_b
if __name__ == '__main__':
    print(evaluate_equality(None, None))        
    print(evaluate_equality(5, 5))              
    print(evaluate_equality("a", "b"))           
    print(evaluate_equality(None, 0))