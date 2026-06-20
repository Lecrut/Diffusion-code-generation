def average_values(d):
    numbers = [v for v in d.values() if isinstance(v, (int, float))]
    if not numbers:
        raise ValueError("No valid numeric values found")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 'text', 'd': 30}
    print(average_values(sample_dict))