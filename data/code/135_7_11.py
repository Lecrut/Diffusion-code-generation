import dis

def check_equivalence(func1, func2):
    code1 = dis.Bytecode(func1)
    code2 = dis.Bytecode(func2)
    return list(code1) == list(code2)

if __name__ == '__main__':
    lambda1 = lambda x: x * 2
    lambda2 = lambda y: y * 2

    print(check_equivalence(lambda1, lambda2))