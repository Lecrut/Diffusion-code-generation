TRUE_VAL = True
FALSE_VAL = False
OPERANDS = [TRUE_VAL, FALSE_VAL]

def compute_or_table():
    results = []
    for first in OPERANDS:
        for second in OPERANDS:
            results.append({"first": first, "second": second, "output": first | second})
    return results

if __name__ == '__main__':
    print(compute_or_table())