def generate_or_truth_table():
    inputs = [True, False]
    table = []
    for p in inputs:
        for q in inputs:
            table.append({"p": p, "q": q, "p OR q": p or q})
    return table

if __name__ == '__main__':
    result = generate_or_truth_table()
    print(result)