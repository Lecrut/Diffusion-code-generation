def get_extremes(numbers):
    return (min(numbers), max(numbers)) if numbers else None

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(get_extremes(sample_values))