def calculate_mean(data):
    if not data:
        return 0
    total_sum = sum(item for s in data for item in s)
    total_count = sum(len(s) for s in data)
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = [
        {1, 2},
        {3, 4, 5},
        {6}
    ]
    print(f"Average: {calculate_mean(sample_data)}")