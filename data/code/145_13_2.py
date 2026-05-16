if __name__ == '__main__':
    data = [
        [True, False],
        [False, True]
    ]
    results = []
    for row in data:
        a = row[0]
        b = row[1]
        nested_expression = (a and (b or False)) or (not a and b)
        result = False
        if a:
            if b:
                result = True
            else:
                result = False
        else:
            if b:
                result = True
            else:
                result = False
        results.append(result)
    print(results)