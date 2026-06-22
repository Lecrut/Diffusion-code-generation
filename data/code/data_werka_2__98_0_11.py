def evaluate_conditions(a, b, c):
    if a and b and c:
        return "All true"
    elif a and b:
        return "A and B true"
    elif a and c:
        return "A and C true"
    elif b and c:
        return "B and C true"
    elif a:
        return "A true"
    elif b:
        return "B true"
    elif c:
        return "C true"
    else:
        return "All false"

if __name__ == '__main__':
    result = evaluate_conditions(True, False, True)
    print(result)