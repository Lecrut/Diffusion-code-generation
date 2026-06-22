def calculate_mean(data):
    if not data:
        return 0
    total_sum = sum(sum(subset) for subset in data)
    total_count = sum(len(subset) for subset in data)
    if total_count == 0:
        return 0
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = [
        {1, 2},
        {3, 4, 5},
        {6}
    ]
    print(f"Mean of sample data: {calculate_mean(sample_data)}")