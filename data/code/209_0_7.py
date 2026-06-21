import statistics

def calculate_average(values):
    return statistics.mean(values)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    avg_value = calculate_average(sample_data)
    print(avg_value)