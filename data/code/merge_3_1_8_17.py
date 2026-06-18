import statistics as stats

def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements,
    where each measurement has an associated category weight (frequency or multiplier).

    Args:
        measurements (list[tuple]): A list of tuples, where each tuple contains 
                                   a numeric value and its corresponding weight.
    
    Returns:
        float: The weighted average rounded to 4 decimal places.
              Raises ValueError if the input is empty or weights are invalid.
    """
    total_weighted_value = sum(value * weight for value, weight in measurements)
    total_weight = sum(weight for _, weight in measurements)

    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")

    return round(total_weighted_value / total_weight, 4)

if __name__ == '__main__':
    # Hard-coded sample values representing weights and their associated categories (multipliers)
    data = [
        (120.5, 3),   # Measurement: 120.5g with weight factor of 3
        (98.7, 4),    # Measurement: 98.7g with weight factor of 4
        (110.2, 2),   # Measurement: 110.2g with weight factor of 2
        (150.0, 6)    # Measurement: 150.0g with weight factor of 6
    ]

    result = calculate_weighted_average(data)
    print(f"Weighted Average: {result}")