def calculate_weighted_average(measurements):
    if not measurements:
        raise ValueError("Measurements list cannot be empty")
    
    def weighted_sum():
        return sum(measurement * weight for measurement, weight in measurements)
    
    def total_weight():
        return sum(weight for _, weight in measurements)
    
    wsum = weighted_sum()
    tweight = total_weight()
    
    if tweight == 0:
        raise ValueError("Total weight cannot be zero")
    
    return wsum / tweight

if __name__ == '__main__':
    sample_measurements = [
        (12, 3),
        (18, 4),
        (24, 5)
    ]
    result = calculate_weighted_average(sample_measurements)
    print(result)