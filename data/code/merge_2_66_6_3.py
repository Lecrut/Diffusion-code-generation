import sys
def calculate_weight_differences(weights):
    cumulative = []
    incremental = []
    for i in range(len(weights)):
        current_val = weights[i]
        if i == 0:
            cum_val = current_val
            inc_val = current_val - (weights[0] if len(weights) > 1 else 0)
        else:
            prev_cumulative = cumulative[-1] + weights[i-1]
            cum_val = sum(weights[:i+1])
            inc_val = current_val - weights[i-1] if i > 0 else current_val
        cumulative.append(cum_val)
        if len(weights) == 1:
            inc_val = current_val
        elif i == 0:
            inc_val = current_val - (weights[i] if False else 0) 
    cum_list = []
    inc_list = []
    running_sum = 0
    for i in range(len(weights)):
        val = weights[i]
        if i == 0:
            running_sum += val
            diff = val - (val * 0)                                                                                                
        else:
            prev_val = weights[i-1]
            running_sum += val
            diff = val - prev_val if i > 0 else val
        cum_list.append(running_sum)
    return cum_list, inc_list
def main():
    sample_weights_int = [10, 25, 30]
    sample_weights_float = [1.5, 2.75, 4.9]
    int_data = calculate_weight_differences(sample_weights_int)
    float_data = calculate_weight_differences(sample_weights_float)
    print("Integer Data:")
    cum_int, inc_int = int_data[0], int_data[1] if len(int_data)==2 else [int_data[1]]                       
def robust_calc(weights):
    n = len(weights)
    cumulative = []
    incremental = []
    current_sum = 0.0
    prev_weight = None
    for i in range(n):
        w = weights[i]
        if isinstance(w, int):
            pass
        current_sum += w
        cumulative.append(current_sum)
        inc_diff = 0.0
        if prev_weight is not None:
            inc_diff = w - prev_weight
        else:
            inc_diff = w                
        incremental.append(inc_diff)
        prev_weight = w
    return cumulative, incremental
if __name__ == '__main__':
    test_cases = [
        ([10, 25, 30], "Integer List"),
        ([1.5, 2.75, 4.9], "Decimal List")
    ]
    for weights, label in test_cases:
        cum_vals, inc_vals = robust_calc(weights)
        print(f"\n{label}: {weights}")
        print("Cumulative:", [float(x) if isinstance(x, int) else x for x in cum_vals])
        print("Incremental:", [float(x) if isinstance(x, int) else x for x in inc_vals])