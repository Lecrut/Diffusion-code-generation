def find_min_max(values):
    return min(values), max(values)

if __name__ == '__main__':
    sample_values = (x**2 for x in range(10))
    print(find_min_max(sample_values))