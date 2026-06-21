def compute_sum(values):
    total = 0
    for value in values:
        total += value
    return total

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(compute_sum(sample_list))