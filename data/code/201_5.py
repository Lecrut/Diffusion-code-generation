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
    if count > 0:
        average = total / count
        return average
    else:
        return 0
if __name__ == '__main__':
    sample_data = [
        "10.5\n",
        "20\n",
        "30.5\n",
        "40\n"
    ]
    with open('data.txt', 'w') as f:
        f.writelines(sample_data)
    average = calculate_average('data.txt')
    print(average)