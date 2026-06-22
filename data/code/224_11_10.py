def calculate_average(sequence):
    if not sequence:
        return 0
    total = sum(sequence)
    count = len(sequence)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    print(calculate_average(sample_values))