def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    return (a and b) or not c

if __name__ == '__main__':
    result = evaluate_logic(True, False, True)
    print(f"Result of (True AND False) OR NOT True: {result}")
    
    result = evaluate_logic(False, False, False)
    print(f"Result of (False AND False) OR NOT False: {result}")
    
    result = evaluate_logic(True, True, False)
    print(f"Result of (True AND True) OR NOT False: {result}")
    
    result = evaluate_logic(False, True, True)
    print(f"Result of (False AND True) OR NOT True: {result}")