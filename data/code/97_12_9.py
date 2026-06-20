def generate_xor_truth_table():
    for a in [0, 1]:
        for b in [0, 1]:
            result = a ^ b
            print(f"{a} XOR {b} = {result}")

if __name__ == '__main__':
    generate_xor_truth_table()