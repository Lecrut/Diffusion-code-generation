def calculate_mean(data):
    if not data:
        return 0
    total_sum = sum(item for sublist in data for item in sublist)
    total_count = sum(len(sublist) for sublist in data)
    if total_count == 0:
        return 0
    return total_sum / total_count

if __name__ == '__main__':
    data = [
        [1, 2],
        [3, 4, 5],
        [6]
    ]
    print(f"Average: {calculate_mean(data)}")