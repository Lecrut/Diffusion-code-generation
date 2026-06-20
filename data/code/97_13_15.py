def generate_and_truth_table():
    inputs = [True, False]
    results = []
    for a in inputs:
        for b in inputs:
            and_result = a and b
            results.append((a, b, and_result))
    return results

if __name__ == '__main__':
    truth_table = generate_and_truth_table()
    for combo in truth_table:
        print(f"{combo[0]} AND {combo[1]} = {combo[2]}")