BOOL_TRUE = True
BOOL_FALSE = False

def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    print(compare_booleans(BOOL_TRUE, BOOL_FALSE))
    print(compare_booleans(BOOL_FALSE, BOOL_FALSE))
    print(compare_booleans(BOOL_TRUE, BOOL_TRUE))