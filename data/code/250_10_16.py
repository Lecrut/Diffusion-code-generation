import statistics

def compute_mean(values):
    return statistics.mean(values)

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [10.5, 20.5, 30.5]
    sample3 = [-10, 20, 30]
    print(f"Mean of {sample1}: {compute_mean(sample1)}")
    print(f"Mean of {sample2}: {compute_mean(sample2)}")
    print(f"Mean of {sample3}: {compute_mean(sample3)}")