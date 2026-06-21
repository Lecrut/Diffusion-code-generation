BOOL_A = True
BOOL_B = False

def compare_booleans(a: bool, b: bool) -> int:
    return int(a ^ b)

if __name__ == '__main__':
    result = compare_booleans(BOOL_A, BOOL_B)
    print(result)