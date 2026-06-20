import dis
SAMPLE_VALUES = [10, 20]

def get_bytecode(func):
    return dis.Bytecode(func)

def are_equivalent(lambda1, lambda2):
    bytecode1 = get_bytecode(lambda1)
    bytecode2 = get_bytecode(lambda2)
    return bytecode1 == bytecode2

def check_functions():
    lambda1 = lambda x: x * 2
    lambda2 = lambda y: y * 2
    print('Lambda functions are equivalent:', are_equivalent(lambda1, lambda2))
if __name__ == '__main__':
    check_functions()