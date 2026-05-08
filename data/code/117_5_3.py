def calculate_difference(file1_path, file2_path, result_path):
    with open(file1_path, 'r') as f1:
        amount1 = float(f1.read().strip())
    with open(file2_path, 'r') as f2:
        amount2 = float(f2.read().strip())
    difference = amount1 - amount2
    with open(result_path, 'w') as f_result:
        f_result.write(str(difference))
if __name__ == '__main__':
    file1 = "input1.txt"
    file2 = "input2.txt"
    result = "output.txt"
    with open(file1, 'w') as f:
        f.write("100.5")
    with open(file2, 'w') as f:
        f.write("45.2")
    calculate_difference(file1, file2, result)
    with open(result, 'r') as f:
        print(f.read())