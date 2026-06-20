def find_out_of_range_weights(weights, min_weight=50, max_weight=200):
    out_of_range = []
    for w in weights:
        if w < min_weight or w > max_weight:
            out_of_range.append(w)
    return out_of_range

def process_large_dataset(weights_data):
    total_count = len(weights_data)
    in_range_count = 0
    out_of_range_list = []
    for weight in weights_data:
        if 50 <= weight <= 200:
            in_range_count += 1
        else:
            out_of_range_list.append(weight)
    return {'total': total_count, 'in_range': in_range_count, 'out_of_range': out_of_range_list}
if __name__ == '__main__':
    sample_weights = [45, 52, 89, 150, 210, 300, 60, 75, 180, 250, 100, 40, 199, 201, 50, 200, -10, 0, 1000]
    result = process_large_dataset(sample_weights)
    print(result)
    oof_result = find_out_of_range_weights(sample_weights)
    print(oof_result)