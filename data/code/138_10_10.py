def and_operation(a, b):
    return a and b

def or_operation(a, b):
    return a or b

def not_operation(a):
    return not a

def nand_operation(a, b):
    return not (a and b)

def nor_operation(a, b):
    return not (a or b)

def xor_operation(a, b):
    return a and (not b) or (not a and b)

def xnor_operation(a, b):
    return not a ^ b
logic_operations = {'AND': and_operation, 'OR': or_operation, 'NOT': not_operation, 'NAND': nand_operation, 'NOR': nor_operation, 'XOR': xor_operation, 'XNOR': xnor_operation}
if __name__ == '__main__':
    A = [True, False]
    B = [True, False]
    print('A | B | A AND B')
    print('---|---|---------')
    for a in A:
        for b in B:
            result = and_operation(a, b)
            print(f'{a} | {b} | {result}')
    print('\nA | B | A OR B')
    print('---|---|--------')
    for a in A:
        for b in B:
            result = or_operation(a, b)
            print(f'{a} | {b} | {result}')
    print('\nA | A NOT')
    print('---|------')
    for a in A:
        result = not_operation(a)
        print(f'{a} | {result}')
    print('\nA | B | A NAND B')
    print('---|---|----------')
    for a in A:
        for b in B:
            result = nand_operation(a, b)
            print(f'{a} | {b} | {result}')
    print('\nA | B | A NOR B')
    print('---|---|---------')
    for a in A:
        for b in B:
            result = nor_operation(a, b)
            print(f'{a} | {b} | {result}')
    print('\nA | B | A XOR B')
    print('---|---|--------')
    for a in A:
        for b in B:
            result = xor_operation(a, b)
            print(f'{a} | {b} | {result}')
    print('\nA | B | A XNOR B')
    print('---|---|---------')
    for a in A:
        for b in B:
            result = xnor_operation(a, b)
            print(f'{a} | {b} | {result}')