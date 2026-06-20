def short_circuit_evaluation():
    a = True
    b = False
    c = True
    result1 = a and b or c
    result2 = not (a or b) and c
    return (result1, result2)
if __name__ == '__main__':
    print(short_circuit_evaluation())