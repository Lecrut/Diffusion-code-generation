def generate_and_truth_table():
    inputs = {True: "True", False: "False"}
    results = []
    for a in inputs:
        for b in inputs:
            and_result = a and b
            results.append((a, b, and_result))
    return results

if __name__ == '__main__':
    truth_table = generate_and_truth_table()
    for row in truth_table:
        print(f"{inputs[row[0]]} AND {inputs[row[1]]} = {inputs[row[2]]}")