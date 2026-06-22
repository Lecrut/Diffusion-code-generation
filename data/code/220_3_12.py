def calculate_mean(data):
    total_sum = sum(sum(subset) for subset in data)
    total_count = sum(len(subset) for subset in data)
    return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    sample_data = [
        [1, 2],
        [3, 4, 5],
        [6]
    ]
    print(f"Mean of sample data: {calculate_mean(sample_data)}")