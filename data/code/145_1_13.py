def nested_logic():
    a = True
    b = False
    c = True

    result1 = not (a and (b or c))
    result2 = (a and not b) or c
    result3 = not ((a and b) or (not c))

    return result1, result2, result3

if __name__ == '__main__':
    results = nested_logic()
    print(results)