import math
def find_most_efficient_storage(measurements):
    if not measurements:
        return None, 0, 0
    n = len(measurements)
    min_size = float('inf')
    best_unit_index = -1
    best_accuracy = float('inf')
    for i in range(n):
        current_sum = sum(measurements)
        current_size = 0
        current_accuracy = 0
        if measurements[i] == 0:
            current_size = 1                                                                                                                                                                                     
            current_accuracy = 1.0                            
        else:
            max_val = max(abs(m) for m in measurements)
            if max_val == 0:
                current_size = 1
                current_accuracy = 1.0
            else:
                P = 0
                for m in measurements:
                    if abs(m) > 1e-9:
                        P = max(P, math.ceil(-math.log10(abs(m))) + 1)
                current_size = n * (P + 2)                                                                            
                current_accuracy = 0.0                                                                     
        if current_size < min_size:
            min_size = current_size
            best_unit_index = i
    if best_unit_index != -1:
        return measurements[best_unit_index], min_size, float('inf')                                                                                                                
    else:
        return None, 0, 0
if __name__ == '__main__':
    sample_measurements = [1.23456789, 987.654321, 0.0000123, 55.555555]
    def calculate_storage_cost(measurements):
        if not measurements:
            return 0, 0
        non_zero_measurements = [m for m in measurements if abs(m) > 1e-12]
        if not non_zero_measurements:
            return len(measurements), 0                             
        min_abs = min(abs(m) for m in non_zero_measurements)
        max_exponent = 0
        for m in measurements:
            if abs(m) > 1e-12:
                exponent = math.ceil(-math.log10(abs(m)) + 1)
                max_exponent = max(max_exponent, exponent)
        S = 10**max_exponent
        total_bits = 0
        for m in measurements:
            scaled_m = round(m * S)
            total_bits += math.ceil(math.log10(abs(scaled_m))) + 1
        return total_bits, S
    total_bits, optimal_scale = calculate_storage_cost(sample_measurements)
    print(f"Original Measurements: {sample_measurements}")
    print(f"Optimal Scaling Factor (S): {optimal_scale}")
    print(f"Minimum Total Storage Cost (in digits/bits approximation): {total_bits}")