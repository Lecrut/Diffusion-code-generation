def calculate_mean(data):
    if not data:
        return 0.0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")