def logical_truth_table(first, second):
    results = {}
    results["A"] = first
    results["B"] = second
    results["A AND B"] = bool(first and second)
    results["A OR B"] = bool(first or second)
    results["A XOR B"] = bool(first != second)
    results["A NAND B"] = not bool(first and second)
    results["A NOR B"] = not bool(first or second)
    results["NOT A"] = not first
    results["NOT B"] = not second
    results["A IMPLIES B"] = bool((not first) or second)
    results["B IMPLIES A"] = bool((not second) or first)
    results["A EQUIV B"] = bool(first == second)
    return results

if __name__ == '__main__':
    output = logical_truth_table(True, False)
    print(output)