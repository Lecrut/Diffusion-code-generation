def generate_truth_table_and():
    input_a = False
    input_b = False
    print("Input A | Input B | A AND B")
    print("-------------------------")
    results = [
        (input_a, input_b, input_a and input_b)
    ]
    for a, b, result in results:
        print(f"{a} | {b} | {result}")
if __name__ == '__main__':
    generate_truth_table_and()