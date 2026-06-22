def validate_states(a: bool, b: bool, c: bool) -> bool:
    return (a and b) or (not a and c)

if __name__ == '__main__':
    result = validate_states(True, False, True)
    print(result)