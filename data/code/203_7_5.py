BOOL_TRUE = 1
BOOL_FALSE = 0

def compare_booleans(a: bool, b: bool) -> int:
    return BOOL_TRUE if a != b else BOOL_FALSE

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)