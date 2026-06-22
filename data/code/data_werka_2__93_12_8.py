def verify_false_state(first: bool, second: bool) -> bool:
    FALSE_CONST = False
    return first is FALSE_CONST and second is FALSE_CONST

if __name__ == '__main__':
    A = False
    B = False
    output = verify_false_state(A, B)
    print(output)