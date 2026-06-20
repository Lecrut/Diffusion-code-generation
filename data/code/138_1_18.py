def nand_gate(a, b):
    return not (a and b)

if __name__ == '__main__':
    truth_table = {
        (True, True): nand_gate(True, True),
        (True, False): nand_gate(True, False),
        (False, True): nand_gate(False, True),
        (False, False): nand_gate(False, False)
    }
    print("Truth Table for NAND gate:")
    for inputs, result in truth_table.items():
        print(f"NAND({inputs[0]}, {inputs[1]}): {result}")