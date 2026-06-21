def compute_average(values):
    total = sum(x for x in values)
    count = len(values)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_values = [50, 60, 70]
    avg_result = compute_average(sample_values)
    print(avg_result)