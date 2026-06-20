import dis

def are_lambda_equivalent(l1, l2):
    return dis.Bytecode(l1) == dis.Bytecode(l2)

if __name__ == '__main__':
    lambda1 = lambda x: x + 1
    lambda2 = lambda x: x + 1
    print(are_lambda_equivalent(lambda1, lambda2))