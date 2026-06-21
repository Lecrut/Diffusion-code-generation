import statistics

def compute_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [25, 30, 45, 60]
    empty_list = []
    single_value = [100]

    mean_sample = compute_mean(sample_data)
    mean_empty = compute_mean(empty_list)
    mean_single = compute_mean(single_value)

    print(f"Mean of {sample_data}: {mean_sample}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {single_value}: {mean_single}")