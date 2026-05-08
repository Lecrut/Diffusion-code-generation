if __name__ == '__main__':
    data = [
        [True, False],
        [False, True]
    ]
    results = []
    for row in data:
        a = row[0]
        b = row[1]
        condition1 = (a and not b) or (not a and b)
        condition2 = a or b
        condition3 = not (a and b)
        result = {
            "a": a,
            "b": b,
            "cond1": condition1,
            "cond2": condition2,
            "cond3": condition3
        }
        results.append(result)
    print(results)