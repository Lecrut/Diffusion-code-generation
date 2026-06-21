def evaluate_flags(flag_a, flag_b, flag_c):
    if flag_a and flag_b:
        return "A and B active"
    if flag_a and flag_c:
        return "A and C active"
    if flag_b and flag_c:
        return "B and C active"
    if flag_a or flag_b or flag_c:
        return "Single flag active"
    return "No flags active"

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    result = evaluate_flags(val_a, val_b, val_c)
    print(result)
    val_a = False
    val_b = False
    val_c = False
    result = evaluate_flags(val_a, val_b, val_c)
    print(result)