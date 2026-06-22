def calculate_average_weight(weight_dict):
    if not weight_dict:
        return 0.0
    total_weight = sum(weight_dict.values())
    number_of_weights = len(weight_dict)
    average_weight = total_weight / number_of_weights
    return average_weight

if __name__ == '__main__':
    sample_weights = {
        'Alice': 130,
        'Bob': 150,
        'Charlie': 145,
        'David': 160,
        'Eve': 170
    }
    average_weight = calculate_average_weight(sample_weights)
    print(f"The average weight is: {average_weight} pounds")