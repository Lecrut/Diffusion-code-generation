def sum_large_dataset(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total

if __name__ == '__main__':
    print(sum_large_dataset('large_dataset.txt'))