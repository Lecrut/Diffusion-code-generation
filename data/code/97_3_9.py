def generate_truth_table():
    header = "P | Q | P -> Q\n"
    separator = "-" * len(header)
    print(header)
    print(separator)

    for p in [0, 1]:
        for q in [0, 1]:
            implication_result = not p or q
            row = f"{p} | {q} | {int(implication_result)}"
            print(row)

if __name__ == '__main__':
    generate_truth_table()