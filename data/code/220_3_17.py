def calculate_mean(values):
    total_sum = sum(values)
    count = len(values)
    if count == 0:
        return 0
    return total_sum / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(f"Mean of sample data: {calculate_mean(sample_data)}")