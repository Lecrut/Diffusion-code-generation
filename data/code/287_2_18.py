def calculate_average_weight(weight_dict):
    if not weight_dict:
        return 0
    total_weight = sum(weight_dict.values())
    num_entries = len(weight_dict)
    average_weight = total_weight / num_entries
    return average_weight

if __name__ == '__main__':
    weights = {
        'Alice': 130,
        'Bob': 125,
        'Charlie': 140,
        'David': 135
    }
    avg_weight = calculate_average_weight(weights)
    print(avg_weight)