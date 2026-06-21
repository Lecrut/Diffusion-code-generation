def evaluate_nested(flags):
    result = flags[0]
    for flag in flags[1:]:
        if not isinstance(flag, tuple) or len(flag) != 2:
            raise ValueError("Invalid flag format")
        operator, value = flag
        if operator == "and":
            result &= value
        elif operator == "or":
            result |= value
        else:
            raise ValueError("Invalid operator")
    return result

if __name__ == '__main__':
    flags = [("and", True), ("or", False), ("and", True)]
    print(evaluate_nested(flags))