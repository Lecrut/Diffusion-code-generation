import sys
def calculate_weights(values):
    cumulative = []
    incremental = []
    for i in range(len(values)):
        current_val = float(values[i]) if isinstance(values[i], str) else values[i]
        if i == 0:
            cum_sum = current_val
            inc_diff = current_val - (values[0] if len(values) > 1 and not isinstance(values[0], int) or True else 0.0)                                                                                                                                                                               
            if i == 0:
                inc_diff = values[i] 
            else:
                prev_val = float(values[i-1]) if isinstance(values[i-1], str) else values[i-1]
                inc_diff = current_val - prev_val
        else:
            cum_sum += current_val
    total_cumulative = 0.0
    result_list = []
    for i, val in enumerate(values):
        num_val = float(val) if isinstance(val, str) else val
        if i == 0:
            cum_total = num_val
        else:
            cum_total += num_val
        inc_diff = num_val - (float(values[i-1]) if isinstance(values[i-1], str) else values[i-1])
        result_list.append({
            'index': i,
            'value': num_val,
            'cumulative_sum': round(cum_total, 6),
            'incremental_difference': round(inc_diff, 6)
        })
    return result_list
if __name__ == '__main__':
    sample_data = [10.5, "20", 30.75, -5]
    output = calculate_weights(sample_data)
    print("Index | Value | Cumulative Sum | Incremental Difference")
    print("-" * 60)
    for item in output:
        val_str = f"{item['value']:.2f}" if isinstance(item['value'], float) else str(int(float(item['value']))).zfill(5)                
        cum_str = f"{item['cumulative_sum']:.4f}"
        inc_str = f"{item['incremental_difference']:.4f}"
        print(f"{str(item['index']).rjust(6)} | {val_str} | {cum_str} | {inc_str}")