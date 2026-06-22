def truth_table(a, b):
    return {
        "a": a,
        "b": b,
        "a and b": a and b,
        "a or b": a or b,
        "a xor b": a ^ b,
        "not a": not a,
        "not b": not b,
        "a implies b": (not a) or b,
        "b implies a": (not b) or a,
        "a nand b": not (a and b),
        "a nor b": not (a or b)
    }

if __name__ == '__main__':
    result = truth_table(True, False)
    print(result)