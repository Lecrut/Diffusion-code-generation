def evaluate_logic():
    a = True
    b = False
    c = True

    result = (a and b) or (not c)
    return result

if __name__ == '__main__':
    print(evaluate_logic())