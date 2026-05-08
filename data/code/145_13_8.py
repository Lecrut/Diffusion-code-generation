if __name__ == '__main__':
    data = [
        [True, False],
        [False, True],
        [True, True]
    ]
    results = []
    for row in data:
        a = row[0]
        b = row[1]
        condition1 = (a and not b) or (not a and b)
        condition2 = a or b
        condition3 = a and b
        result = {
            "row": row,
            "cond1": condition1,
            "cond2": condition2,
            "cond3": condition3
        }
        results.append(result)
    print("Evaluation Results:")
    for res in results:
        print(f"Row: {res['row']}, Cond1: {res['cond1']}, Cond2: {res['cond2']}, Cond3: {res['cond3']}")