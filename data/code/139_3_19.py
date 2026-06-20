def bitwise_and(a: bool, b: bool) -> bool:
    return a & b

def bitwise_or(a: bool, b: bool) -> bool:
    return a | b

def bitwise_not(a: bool) -> bool:
    return not a

def bitwise_xor(a: bool, b: bool) -> bool:
    return a ^ b

def bitwise_nand(a: bool, b: bool) -> bool:
    return ~(a & b)

def bitwise_nor(a: bool, b: bool) -> bool:
    return ~(a | b)

def bitwise_xnor(a: bool, b: bool) -> bool:
    return ~(a ^ b)

if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    
    results = {
        "AND": [(bitwise_and(a, b), a, b) for a, b in inputs],
        "OR": [(bitwise_or(a, b), a, b) for a, b in inputs],
        "NOT_A": [(bitwise_not(a), a) for a, _ in inputs],
        "NOT_B": [(bitwise_not(b), b) for _, b in inputs],
        "XOR": [(bitwise_xor(a, b), a, b) for a, b in inputs],
        "NAND": [(bitwise_nand(a, b), a, b) for a, b in inputs],
        "NOR": [(bitwise_nor(a, b), a, b) for a, b in inputs],
        "XNOR": [(bitwise_xnor(a, b), a, b) for a, b in inputs]
    }
    
    for operation, result_list in results.items():
        print(f"{operation}:")
        for output in result_list:
            print(output)