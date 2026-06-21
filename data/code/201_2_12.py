def compute_average(*values):
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    sample_values = (15, 25, 35, 45, 55)
    avg_result = compute_average(*sample_values)
    print(avg_result)