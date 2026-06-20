def truth_table(variables):
    num_vars = len(variables)
    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars):
            row.append(bool(i & (1 << j)))
        print(" | ".join(str(x) for x in row))

if __name__ == '__main__':
    truth_table(['A', 'B', 'C'])