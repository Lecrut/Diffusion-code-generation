def calculate_mean(array):
    return sum(array) / len(array)

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    print(calculate_mean(sample_array))