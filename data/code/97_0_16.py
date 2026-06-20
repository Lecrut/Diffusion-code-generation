def generate_truth_table():
    values = [True, False]
    print("P | Q | P AND Q")
    for p in values:
        for q in values:
            result = p and q
            print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    generate_truth_table()