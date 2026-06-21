def generate_truth_table(n):
    truth_table = []
    for i in range(2**n):
        binary = format(i, f'0{n}b')
        inputs = [int(bit) for bit in binary]
        outputs = {f'P{i+1}': input_val for i, input_val in enumerate(inputs)}
        truth_table.append(outputs)
    return truth_table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table(3)
    print(sample_truth_table)