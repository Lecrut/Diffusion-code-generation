import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    sample1 = [2, 4, 6, 8, 10]
    sample2 = [1.5, 2.5, 3.5, 4.5]
    sample3 = [-5, 0, 5, 10]

    print(f"Mean of {sample1}: {compute_mean(sample1)}")
    print(f"Mean of {sample2}: {compute_mean(sample2)}")
    print(f"Mean of {sample3}: {compute_mean(sample3)}")