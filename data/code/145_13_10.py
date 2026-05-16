if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    result = []
    for i in range(5):
        condition1 = (a and b) or (c and not d)
        condition2 = (a or b) and (c and d)
        condition3 = not (a and c) or (b and d)
        condition4 = a if (b and c) else (not d)
        value = []
        if i == 0:
            value.append(condition1)
            value.append(condition2)
            value.append(condition3)
            value.append(condition4)
        elif i == 1:
            value.append(condition1)
            value.append(condition2)
            value.append(condition3)
            value.append(condition4)
        elif i == 2:
            value.append(condition1)
            value.append(condition2)
            value.append(condition3)
            value.append(condition4)
        elif i == 3:
            value.append(condition1)
            value.append(condition2)
            value.append(condition3)
            value.append(condition4)
        elif i == 4:
            value.append(condition1)
            value.append(condition2)
            value.append(condition3)
            value.append(condition4)
        result.append(value)
    print(result)