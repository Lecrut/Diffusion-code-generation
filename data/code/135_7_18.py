import dis

def check_equivalence(func1, func2):
    code1 = dis.Bytecode(func1)
    code2 = dis.Bytecode(func2)
    if len(code1) != len(code2):
        return False
    for instr1, instr2 in zip(code1, code2):
        if instr1 != instr2:
            return False
    return True

def sample_func1(x, y):
    return x + y

def sample_func2(x, y):
    return x + y
if __name__ == '__main__':
    result = check_equivalence(sample_func1, sample_func2)
    print(result)