def boolean_operations():
    results = {
        (True, True): {'AND': True, 'OR': True, 'NOT': False, 'XOR': False, 'NAND': False, 'NOR': False, 'IMPLIES': True},
        (True, False): {'AND': False, 'OR': True, 'NOT': False, 'XOR': True, 'NAND': True, 'NOR': False, 'IMPLIES': False},
        (False, True): {'AND': False, 'OR': True, 'NOT': False, 'XOR': True, 'NAND': True, 'NOR': False, 'IMPLIES': False},
        (False, False): {'AND': False, 'OR': False, 'NOT': True, 'XOR': False, 'NAND': True, 'NOR': True, 'IMPLIES': True}
    }
    return results

if __name__ == '__main__':
    print(boolean_operations())