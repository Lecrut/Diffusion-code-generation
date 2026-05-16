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
        c = a and b
        d = not c
        e = (a or b) and (not c)
        f = a and (b or c)
        g = not a and b
        h = a or b and c
        results.append({
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "e": e,
            "f": f,
            "g": g,
            "h": h
        })
    evaluated_results = []
    for res in results:
        if res["c"] and res["e"]:
            evaluated_results.append("True")
        elif res["f"]:
            evaluated_results.append("True")
        elif res["g"]:
            evaluated_results.append("True")
        else:
            evaluated_results.append("False")
    print(evaluated_results)