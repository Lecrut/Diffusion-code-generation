def calculate_average_weight(weights):
    if not weights:
        return 0.0
    
    total_weight = sum(weights.values())
    average_weight = total_weight / len(weights)
    
    return average_weight

if __name__ == '__main__':
    sample_weights = {
        "Alice": 130,
        "Bob": 150,
        "Charlie": 140
    }
    
    avg_weight = calculate_average_weight(sample_weights)
    print(avg_weight)