def evaluate_equality(input_a: any, input_b: any) -> bool:
    if input_a is None and input_b is None:
        return True
    elif input_a is not None and input_b is not None:
        return input_a == input_b
    else:
        return False
if __name__ == '__main__':
    print(evaluate_equality(None, None))                
    print(evaluate_equality(5, 5))                       
    print(evaluate_equality("hello", "world"))                 
    print(evaluate_equality(None, "test"))