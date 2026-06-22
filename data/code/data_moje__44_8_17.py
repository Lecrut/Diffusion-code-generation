def compute_mean(integers):
    if not integers:
        raise ValueError("List cannot be empty")
    return sum(integers) / len(integers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = compute_mean(sample_values)
    print(result)