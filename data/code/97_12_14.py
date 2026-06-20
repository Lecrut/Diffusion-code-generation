def xor_truth_table():
    inputs = [0, 1]
    print("XOR Truth Table:")
    for a in inputs:
        for b in inputs:
            result = a ^ b
            print(f"{a} XOR {b} = {result}")

if __name__ == '__main__':
    xor_truth_table()