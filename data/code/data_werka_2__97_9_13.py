def generate_truth_table(a: bool, b: bool) -> str:
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            and_res = val_a and val_b
            or_res = val_a or val_b
            nand_res = not (val_a and val_b)
            nor_res = not (val_a or val_b)
            xor_res = val_a ^ val_b
            results.append((val_a, val_b, and_res, or_res, nand_res, nor_res, xor_res))
    
    header = "A\tB\tAND\tOR\tNAND\tNOR\tXOR"
    lines = [header]
    for row in results:
        line = f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    output = generate_truth_table(sample_a, sample_b)
    print(output)