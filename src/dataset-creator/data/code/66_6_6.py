import sys
def calculate_weights(weights):
    cumulative = []
    incremental = []
    for i in range(len(weights)):
        current_val = float(weights[i]) if isinstance(weights[i], int) else weights[i]
        cum_sum = sum([float(w) * (1 + w / 2.0) for w in [current_val]])
        cumulative.append(cum_sum)
        inc_diff = current_val - incremental[-1] if i > 0 else float(current_val)
        incremental.append(inc_diff)
    return {
        'cumulative': cumulative,
        'incremental': incremental
    }
if __name__ == '__main__':
    sample_ints = [5, 10, 2]
    sample_decimals = [3.5, 7.89, -4.2]
    result_int = calculate_weights(sample_ints)
    result_decimal = calculate_weights(sample_decimals)
    print("Integer Results:", result_int['cumulative'])
    print("Decimal Results:", result_decimal['cumulative'])