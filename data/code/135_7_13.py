import dis

def are_lambdas_equivalent(l1, l2):
    return dis.Bytecode(l1).dis() == dis.Bytecode(l2).dis()

if __name__ == '__main__':
    lambda1 = lambda x: x * 2
    lambda2 = lambda y: y * 2
    print(are_lambdas_equivalent(lambda1, lambda2))