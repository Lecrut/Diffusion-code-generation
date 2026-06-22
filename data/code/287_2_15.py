def calculate_average_weight(weight_dict):
    if not weight_dict:
        return 0
    total_weight = sum(weight_dict.values())
    average_weight = total_weight / len(weight_dict)
    return average_weight

if __name__ == '__main__':
    sample_weights = {'Alice': 120, 'Bob': 150, 'Charlie': 130}
    print(calculate_average_weight(sample_weights))