import sys
def calculate_weights(values):
    cumulative = []
    incremental = []
    for i in range(len(values)):
        current_val = float(values[i]) if isinstance(values[i], str) else values[i]
        if i == 0:
            cum_val = current_val
            inc_val = current_val - (current_val if len([v for v in values[:i]]) > 0 else 0)
        else:
            prev_cumulative = cumulative[-1]
            cum_val = prev_cumulative + current_val
            inc_val = current_val - (values[i-1]) if isinstance(values[i], int) or isinstance(values[i], float) else 0
        cumulative.append(cum_val)
    return cumulative
def main():
    sample_data = [5, 2.5, "3", 7]
    processed_values = []
    for item in sample_data:
        if isinstance(item, str):
            try:
                val = float(item)
            except ValueError:
                continue
        else:
            val = float(item)
        processed_values.append(val)
    cumulative_result = [0] * len(processed_values)
    running_sum = 0.0
    for i in range(len(processed_values)):
        current_val = processed_values[i]
        if i == 0:
            cum_val = current_val
        else:
            cum_val = cumulative_result[i-1] + current_val
        incremental_diff = current_val - (processed_values[i-1]) if i > 0 else current_val
        running_sum += current_val
        cumulative_result[i] = running_sum
    print("Cumulative Weights:", [round(x, 2) for x in cumulative_result])
if __name__ == '__main__':
    main()