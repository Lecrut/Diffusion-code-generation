def nand_gate(a, b):
    return not (a and b)

if __name__ == '__main__':
    results = {
        (True, True): nand_gate(True, True),
        (True, False): nand_gate(True, False),
        (False, True): nand_gate(False, True),
        (False, False): nand_gate(False, False)
    }
    
    for inputs, output in results.items():
        print(f"Input: {inputs}, Output: {output}")