def validate_truth_table():
    A_values = [0, 1]
    B_values = [0, 1]

    for a in A_values:
        for b in B_values:
            expression_result = (a and b) or (not a and not b)
            yield (a, b, expression_result)

if __name__ == '__main__':
    print("A | B | Expression Result")
    print("-" * 30)
    for a, b, result in validate_truth_table():
        print(f"{a} | {b} | {result}")