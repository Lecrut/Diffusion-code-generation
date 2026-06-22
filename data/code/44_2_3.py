def arithmetic_mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10.0, 20.0, 30.0, 40.0, 50.0]
    result = arithmetic_mean(sample_values)
    print(result)