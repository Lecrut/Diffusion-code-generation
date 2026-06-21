def generate_truth_table(a: bool, b: bool) -> list:
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            and_res = val_a and val_b
            or_res = val_a or val_b
            nand_res = not (val_a and val_b)
            nor_res = not (val_a or val_b)
            xor_res = val_a ^ val_b
            results.append({
                'A': val_a,
                'B': val_b,
                'A AND B': and_res,
                'A OR B': or_res,
                'A NAND B': nand_res,
                'A NOR B': nor_res,
                'A XOR B': xor_res
            })
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    table = generate_truth_table(sample_a, sample_b)
    for row in table:
        print(row)