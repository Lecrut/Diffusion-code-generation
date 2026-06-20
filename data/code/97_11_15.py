def generate_truth_table(input_combinations):
    for combination in input_combinations:
        a, b = combination
        result = a or b
        print(f"a: {a}, b: {b} -> Result: {result}")

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    generate_truth_table(sample_inputs)