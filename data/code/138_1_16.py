def nand_gate(a, b):
    return not (a and b)

if __name__ == '__main__':
    input1 = True
    input2 = False
    result = nand_gate(input1, input2)
    print(f"NAND({input1}, {input2}) = {result}")