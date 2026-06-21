def generate_truth_table():
    truth_table = []
    for a in range(2):
        for b in range(2):
            result = 'T' if (not a) or b else 'F'
            truth_table.append((a, b, result))
    return truth_table

if __name__ == '__main__':
    sample_a = 0
    sample_b = 1
    table = generate_truth_table()
    print(f"A\tB\tA->B")
    for row in table:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")