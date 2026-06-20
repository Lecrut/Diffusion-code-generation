def generate_truth_table():
    print("P | Q | P -> Q")
    for p in [False, True]:
        for q in [False, True]:
            result = not p or q
            print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    generate_truth_table()