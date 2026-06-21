def compute_sum(elements):
    total = 0
    for element in elements:
        total += element
    return total

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25]
    print(compute_sum(sample_values))