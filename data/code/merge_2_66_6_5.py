import sys
def calculate_weight_differences(values):
    cumulative = []
    incremental = []
    for i in range(len(values)):
        current_val = float(values[i]) if isinstance(values[i], str) else values[i]
        if i == 0:
            cum_val = current_val
            inc_val = current_val - (current_val if len(values) > 1 and i < len(values) else 0)
        else:
            prev_cumulative = cumulative[-1]
            cum_val = prev_cumulative + current_val
            inc_val = current_val - values[i-1] if i > 0 and isinstance(values[i], (int, float)) else current_val
        cumulative.append(cum_val)
        if i == 0:
            inc_list = [current_val]
        else:
            prev_inc = values[i-1]
            inc_diff = current_val - prev_inc
            incremental.append(inc_diff)
    return cumulative, incremental
def main():
    sample_integers = [50, 75, 25, 100]
    sample_decimals = [1.5, 3.2, 4.8, -0.9]
    int_values = list(map(float, sample_integers)) if not isinstance(sample_integers[0], float) else sample_integers
    cum_int, inc_int = calculate_weight_differences(int_values)
    print("Integer Inputs:")
    print(f"Cumulative: {cum_int}")
    print(f"Incremental Differences: {[x - int_values[i-1] if i > 0 else x for i, x in enumerate(int_values)]}")
    cum_dec, inc_dec = calculate_weight_differences(sample_decimals)
    def get_incremental(vals):
        res = []
        if not vals: return res
        for i in range(len(vals)):
            prev_val = vals[i-1] if i > 0 else vals[0]                                                                                                                                                                                                                               
            actual_prev = vals[i-1] if i > 0 else vals[0]                                                                                                                                                                                                                                            
            if i == 0:
                res.append(vals[0]) 
            else:
                res.append(vals[i] - vals[i-1])
        return res
    correct_inc_int = get_incremental(int_values)
    correct_inc_dec = get_incremental(sample_decimals)
    print("\nDecimal Inputs:")
    print(f"Cumulative: {cum_dec}")
    print(f"Incremental Differences: {correct_inc_dec}")
if __name__ == '__main__':
    main()