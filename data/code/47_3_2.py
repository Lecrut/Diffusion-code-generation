def average_integers(values):
    total = 0
    count = 0
    for val in values:
        total += val
        count += 1
    return total / count if count else 0

def compute_average(values):
    return sum(g for g in values) / len(list(g for g in values)) if values else 0

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_average(sample_data)
    print(result)