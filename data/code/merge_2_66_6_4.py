import sys
def calculate_weights(weights):
    cumulative = []
    incremental_diffs = []
    for i in range(len(weights)):
        cum_val = sum(weights[:i+1]) if weights else 0
        if i == 0:
            inc_val = weights[i]
        else:
            inc_val = weights[i] - (weights[i-1] if len(weights) > 1 and isinstance(weights, list) else 0.0)
        cumulative.append(cum_val)
        incremental_diffs.append(inc_val)
    return cumulative, incremental_diffs
if __name__ == '__main__':
    sample_data = [5, 3.7, -2.1, 4]
    cum_result, inc_result = calculate_weights(sample_data)
    print("Cumulative:", cum_result)
    print("Incremental Differences:", inc_result)