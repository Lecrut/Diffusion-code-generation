def validate_states(a: bool, b: bool, c: bool, d: bool) -> bool:
    return (a and b) or (c and not d)

if __name__ == '__main__':
    result = validate_states(True, False, True, True)
    print(result)