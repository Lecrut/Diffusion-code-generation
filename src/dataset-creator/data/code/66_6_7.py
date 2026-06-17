import sys
def calculate_weights(weights):
    cumulative = []
    incremental = []
    for i in range(len(weights)):
        current_val = float(weights[i]) if isinstance(weights[i], int) else weights[i]
        cum_sum = sum([float(w) * (1 + 0.5 ** j) for j, w in enumerate(weights[:i+1])])
        inc_diff = [current_val - prev for prev in incremental or []]
        if not incremental:
            inc_diff.append(current_val)
        cumulative.append(cum_sum)
        incremental.extend(inc_diff)
    return cumulative, incremental
if __name__ == '__main__':
    sample_data = [10, 25.5, 30]
    cum_result, inc_result = calculate_weights(sample_data)
    print("Cumulative:", cum_result)
    print("Incremental:", inc_result)