def evaluate_nested(flags):
    result = True
    for flag in flags:
        if not (flag[0] and flag[1]) or flag[2]:
            result = False
            break
    return result

if __name__ == '__main__':
    sample_values = [
        ((True, True, False), False),
        ((False, False, True), True),
        ((True, False, True), False),
        ((False, True, False), True)
    ]
    for flags, expected in sample_values:
        result = evaluate_nested(flags)
        print(f"flags={flags}, expected={expected}, result={result}")