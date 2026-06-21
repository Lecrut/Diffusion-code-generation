def precedence_and_associativity():
    a = True
    b = False
    c = True

    result = not (a and b) or c
    return result

if __name__ == '__main__':
    print(precedence_and_associativity())