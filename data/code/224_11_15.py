def calculate_average(sequence):
    total = sum(sequence)
    count = len(sequence)
    average = total / count
    return average

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    result = calculate_average(sample_sequence)
    print(result)