def generate_xor_truth_table():
    inputs = [0, 1]
    print(f"{'Input A':<6} {'Input B':<6} {'Output':<6}")
    for a in inputs:
        for b in inputs:
            output = int(a != b)
            print(f"{a:<6} {b:<6} {output:<6}")

if __name__ == '__main__':
    generate_xor_truth_table()