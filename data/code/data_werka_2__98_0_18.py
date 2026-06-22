def evaluate_conditions(a, b, c, d):
    if a and b:
        return "Both a and b are true"
    elif c or d:
        return "Either c or d is true"
    elif not a and not b:
        return "Neither a nor b is true"
    else:
        return "Default case"

if __name__ == '__main__':
    result = evaluate_conditions(True, False, True, False)
    print(result)