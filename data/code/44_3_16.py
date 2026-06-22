DEFAULT_ZERO_VALUE = 0

SAMPLE_LIST = [15, 25, 35, 45, 55]

def compute_average(values):
    count = len(values)
    if count == 0:
        return DEFAULT_ZERO_VALUE
    total_sum = sum(values)
    return total_sum / count

if __name__ == '__main__':
    result = compute_average(SAMPLE_LIST)
    print(result)