import dis

def are_lambdas_equivalent(lambda1, lambda2):
    return dis.Bytecode(lambda1) == dis.Bytecode(lambda2)

if __name__ == '__main__':
    sample_arg = 42
    lambda1 = lambda x: x * 2
    lambda2 = lambda x: x * 2
    print(are_lambdas_equivalent(lambda1, lambda2))