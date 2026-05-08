if __name__ == '__main__':
    data = [
        [True, False],
        [False, True]
    ]
    results = []
    for row in data:
        result = (row[0] and (row[1] or not row[0])) if row[0] else (not row[1])
        results.append(result)
    print(results)