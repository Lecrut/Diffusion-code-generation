def calculate_average_weight(weight_dict):
    if not weight_dict:
        return 0.0
    total_weight = sum(weight_dict.values())
    num_entries = len(weight_dict)
    average_weight = total_weight / num_entries
    return average_weight

if __name__ == '__main__':
    sample_weights = {'Alice': 120, 'Bob': 150, 'Charlie': 130}
    print(calculate_average_weight(sample_weights))