STATISTICS_CONFIG = {
    "operation": "mean",
    "description": "Calculate arithmetic mean"
}

def compute_arithmetic_mean(integers):
    if not integers:
        return 0.0
    total_sum = sum(integers)
    element_count = len(integers)
    return total_sum / element_count

if __name__ == '__main__':
    hardcoded_data = [12, 24, 36, 48, 60]
    mean_value = compute_arithmetic_mean(hardcoded_data)
    print(mean_value)