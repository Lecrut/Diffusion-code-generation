def generate_truth_table(inputs):
    if not inputs:
        return
    n = len(inputs)
    header = " | ".join(inputs)
    print(header)
    print("-" * len(header))
    for i in range(1 << n):
        row = []
        for j in range(n):
            val = (i >> (n - 1 - j)) & 1
            row.append(str(bool(val)))
        print(" | ".join(row))

if __name__ == '__main__':
    generate_truth_table(["P", "Q"])