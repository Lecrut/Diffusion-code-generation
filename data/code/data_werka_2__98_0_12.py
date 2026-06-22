def evaluate_conditions(a, b, c):
    if a and b and c:
        return "All True"
    elif a and b:
        return "A and B True"
    elif a and c:
        return "A and C True"
    elif b and c:
        return "B and C True"
    elif a:
        return "Only A True"
    elif b:
        return "Only B True"
    elif c:
        return "Only C True"
    else:
        return "All False"

if __name__ == '__main__':
    result = evaluate_conditions(True, False, True)
    print(result)