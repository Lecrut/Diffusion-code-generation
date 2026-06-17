import math
def find_most_weight_efficient_storage(measurements):
    if not measurements:
        return None, 0.0
    n = len(measurements)
    min_weight = float('inf')
    best_storage_method = None
    for i in range(n):
        current_measurement = measurements[i]
        weight_float = 8                                                       
        if isinstance(current_measurement, (int, float)):
            if isinstance(current_measurement, int):
                required_bits = current_measurement.bit_length()
            else:
                if current_measurement == 0.0:
                    required_bits = 1                      
                else:
                    required_bits = 64                                     
            current_weight = required_bits
        else:
            continue
        if current_weight < min_weight:
            min_weight = current_weight
            best_storage_method = (i, current_measurement, current_weight)
    return best_storage_method
if __name__ == '__main__':
    sample_measurements = [10.5, 3.14159, 1234567890123.45, -0.0001, 5000000000]
    result = find_most_weight_efficient_storage(sample_measurements)
    if result:
        index, value, weight = result
        print(f"Most weight-efficient unit found:")
        print(f"Index: {index}")
        print(f"Value: {value}")
        print(f"Minimum Weight (bits required): {weight}")
    else:
        print("No measurements provided.")