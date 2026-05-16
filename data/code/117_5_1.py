def calculate_difference(file1_path, file2_path, result_path):
    with open(file1_path, 'r') as f1:
        amount1 = float(f1.read().strip())
    with open(file2_path, 'r') as f2:
        amount2 = float(f2.read().strip())
    difference = amount1 - amount2
    with open(result_path, 'w') as rf:
        rf.write(str(difference))
if __name__ == '__main__':
    file1 = "amounts1.txt"
    file2 = "amounts2.txt"
    result = "difference.txt"
    with open(file1, 'w') as f:
        f.write("100.5")
    with open(file2, 'w') as f:
        f.write("45.2")
    calculate_difference(file1, file2, result)