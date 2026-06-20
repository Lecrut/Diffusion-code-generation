def nand_gate(a, b):
    return not (a and b)

if __name__ == '__main__':
    print(f"NAND(True, True): {nand_gate(True, True)}")
    print(f"NAND(True, False): {nand_gate(True, False)}")
    print(f"NAND(False, True): {nand_gate(False, True)}")
    print(f"NAND(False, False): {nand_gate(False, False)}")