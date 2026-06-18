import sys
def calculate_weight_diffs(weights):
    cumulative = []
    incremental = []
    for i in range(len(weights)):
        current_val = weights[i]
        if i == 0:
            cum_sum = current_val
        else:
            cum_sum = sum(weights[:i+1])
        inc_diff = current_val - (weights[i-1] if i > 0 else 0)
        cumulative.append(cum_sum)
        incremental.append(inc_diff)
    return cumulative, incremental
if __name__ == '__main__':
    sample_data = [5.234, 789, -12.3456, 0]
    cum_res, inc_res = calculate_weight_diffs(sample_data)
    print(f"Cumulative: {cum_res}")
    print(f"Incremental: {inc_res}")