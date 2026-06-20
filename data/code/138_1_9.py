def nand_gate(a, b):
    return not (a and b)

if __name__ == '__main__':
    result1 = nand_gate(True, True)
    result2 = nand_gate(True, False)
    result3 = nand_gate(False, True)
    result4 = nand_gate(False, False)
    
    print(f"NAND(True, True): {result1}")
    print(f"NAND(True, False): {result2}")
    print(f"NAND(False, True): {result3}")
    print(f"NAND(False, False): {result4}")