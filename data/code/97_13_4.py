def generate_truth_table():
    inputs = [True, False]
    print("A | B | A AND B")
    for a in inputs:
        for b in inputs:
            result = a and b
            print(f"{a} | {b} | {result}")

if __name__ == '__main__':
    generate_truth_table()