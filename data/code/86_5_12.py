def compare_booleans(a: bool, b: bool) -> tuple:
    operations = {'==': (a == b)}
    return operations['=='], '=='

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)