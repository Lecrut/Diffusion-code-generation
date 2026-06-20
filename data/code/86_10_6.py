BOOL_EQ = "Equal"
BOOL_DIFF = "Different"

def compare_booleans(a: bool, b: bool) -> str:
    return BOOL_EQ if a == b else BOOL_DIFF

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))