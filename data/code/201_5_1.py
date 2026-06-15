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
    with open('data.txt', 'w') as f:
        f.write("10\n")
        f.write("20\n")
        f.write("30\n")
        f.write("40\n")
    average = calculate_average('data.txt')
    print(average)