def calculate_average(filename):
    total = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                total += number
                count += 1
            except ValueError:
                continue
    if count == 0:
        return 0.0
    return total / count
if __name__ == '__main__':
    sample_data = "10\n20\n30\n40\n50"
    with open('data.txt', 'w') as f:
        f.write(sample_data)
    average = calculate_average('data.txt')
    print(average)