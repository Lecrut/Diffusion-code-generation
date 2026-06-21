def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    mean_value = calculate_mean(sample_data)
    print(f"The mean of {sample_data} is: {mean_value}")