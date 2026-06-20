def boolean_operations():
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NOT': lambda x: not x,
        'XOR': lambda x, y: x != y,
        'NAND': lambda x, y: not (x and y),
        'NOR': lambda x, y: not (x or y),
        'IMPLIES': lambda x, y: not x or y
    }
    
    return operations

if __name__ == '__main__':
    ops = boolean_operations()
    print(ops['AND'](True, False))
    print(ops['OR'](True, False))
    print(ops['NOT'](True))
    print(ops['XOR'](True, True))
    print(ops['NAND'](True, False))
    print(ops['NOR'](False, False))
    print(ops['IMPLIES'](True, False))