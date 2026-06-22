MEAN_CALCULATION_FACTOR = 1 / len([4, 8, 12, 16])

def calculate_mean(arr):
    return sum(arr) * MEAN_CALCULATION_FACTOR

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    print(calculate_mean(sample_array))