def compute_average(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_data = [3.5, 2.1, 4.8, 6.0]
    average = compute_average(sample_data)
    print(average)