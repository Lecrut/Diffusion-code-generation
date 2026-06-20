def bitwise_logic_and(a: bool, b: bool) -> bool:
    return a & b

def bitwise_logic_or(a: bool, b: bool) -> bool:
    return a | b

def bitwise_logic_not(a: bool) -> bool:
    return not a
if __name__ == '__main__':
    print(bitwise_logic_and(True, False))
    print(bitwise_logic_or(False, True))
    print(bitwise_logic_not(True))