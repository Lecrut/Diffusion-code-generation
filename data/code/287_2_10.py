def calculate_average_weight(weights):
    if not weights:
        return 0
    total_weight = sum(weights.values())
    number_of_weights = len(weights)
    average_weight = total_weight / number_of_weights
    return average_weight

if __name__ == '__main__':
    sample_weights = {'Alice': 120, 'Bob': 150, 'Charlie': 130}
    print(calculate_average_weight(sample_weights))