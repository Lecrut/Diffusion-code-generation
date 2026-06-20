def generate_xor_truth_table():
    values = [0, 1]
    print("XOR Truth Table:")
    for v1 in values:
        for v2 in values:
            result = v1 ^ v2
            print(f"{v1} XOR {v2} = {result}")

if __name__ == '__main__':
    generate_xor_truth_table()