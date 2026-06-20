TRUE = True
FALSE = False

def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return f"{a} is equal to {b}"
    else:
        return f"{a} is not equal to {b}"

if __name__ == '__main__':
    result = compare_booleans(TRUE, FALSE)
    print(result)