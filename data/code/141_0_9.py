def bitwise_and(a: bool, b: bool) -> bool:
    return a & b

def bitwise_or(a: bool, b: bool) -> bool:
    return a | b

def bitwise_not(a: bool) -> bool:
    return not a
if __name__ == '__main__':
    A_val = False
    B_val = True
    output_and = bitwise_and(A_val, B_val)
    output_or = bitwise_or(A_val, B_val)
    output_not = bitwise_not(B_val)
    print(output_and)
    print(output_or)
    print(output_not)