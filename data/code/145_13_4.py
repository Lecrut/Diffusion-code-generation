if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    results = []
    for i in range(5):
        condition1 = (a and b) or (c and not d)
        condition2 = (a or b) and (c and d)
        condition3 = not (a and not b) or (c and d)
        condition4 = (a and c) or (b and d)
        result = []
        if condition1:
            result.append("C1: True")
        else:
            result.append("C1: False")
        if condition2:
            result.append("C2: True")
        else:
            result.append("C2: False")
        if condition3:
            result.append("C3: True")
        else:
            result.append("C3: False")
        if condition4:
            result.append("C4: True")
        else:
            result.append("C4: False")
        results.append(result)
    for res_set in results:
        print(f"Iteration {res_set}: {res_set}")