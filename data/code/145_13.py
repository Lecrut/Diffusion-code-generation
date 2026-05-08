if __name__ == '__main__':
    data = [
        [True, False],
        [False, True]
    ]
    results = []
    for row in data:
        result = []
        for i in range(len(row)):
            a = row[i]
            b = row[i+1] if i + 1 < len(row) else False
            if a and b:
                result.append(True)
            elif a or b:
                result.append(False)
            else:
                result.append(False)
        results.append(result)
    print(results)