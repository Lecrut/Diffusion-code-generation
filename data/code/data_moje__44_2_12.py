def arithmetic_mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.7, 40.1, 50.9]
    result = arithmetic_mean(sample_values)
    print(result)