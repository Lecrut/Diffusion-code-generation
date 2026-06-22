def find_extremes(numbers):
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    smallest, largest = find_extremes(sample_values)
    print(f"Smallest: {smallest}, Largest: {largest}")