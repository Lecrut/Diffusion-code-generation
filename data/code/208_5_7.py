MEAN_CALCULATION = lambda data: sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    print(f"Mean of {sample_data}: {MEAN_CALCULATION(sample_data)}")