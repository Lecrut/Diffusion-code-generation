import statistics

def calculate_mean(values):
    if not values:
        return None
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))
    empty_list = []
    print(calculate_mean(empty_list))