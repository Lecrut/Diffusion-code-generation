def calculate_difference(file1_path, file2_path, result_path):
    with open(file1_path, 'r') as f1:
        amount1 = float(f1.read().strip())
    with open(file2_path, 'r') as f2:
        amount2 = float(f2.read().strip())
    difference = amount1 - amount2
    with open(result_path, 'w') as fr:
        fr.write(str(difference))
if __name__ == '__main__':
    with open('input1.txt', 'w') as f:
        f.write("100.5")
    with open('input2.txt', 'w') as f:
        f.write("45.2")
    calculate_difference('input1.txt', 'input2.txt', 'result.txt')