BOOL1 = True
BOOL2 = False

def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    result = compare_booleans(BOOL1, BOOL2)
    print(result)