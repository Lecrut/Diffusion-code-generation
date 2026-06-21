def implication(a: bool, b: bool) -> bool:
    return not a or b

if __name__ == '__main__':
    for A in (False, True):
        for B in (False, True):
            result = implication(A, B)
            print(f"A={A} | B={B} | {A} IMPLIES {B} = {result}")