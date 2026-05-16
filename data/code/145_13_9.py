if __name__ == '__main__':
    data = [
        [True, False],
        [False, True]
    ]
    results = []
    for row in data:
        a = row[0]
        b = row[1]
        inner_condition = (a and not b) or (not a and b)
        outer_condition = inner_condition and (a or b)
        result = "True" if outer_condition else "False"
        results.append(result)
    print(results)