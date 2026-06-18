import statistics

def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C).
    
    Args:
        temperatures (list[float]): A list of floating-point temperature values in Celsius.
        
    Returns:
        list[float]: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing a large dataset of simulated readings
    raw_readings = [-5, -12.3, 0, 4.5, -7, 8.9, -0.1, 15.6] * (len(raw_readings) // len([-5, -12.3, 0, 4.5, -7, 8.9, -0.1, 15.6]))
    
    # Ensure we have enough data to simulate "large" efficiently without external input
    while len(raw_readings) < 1_000_000:
        raw_readings.extend([-20 + statistics.mean(list(range(-30, -8))) for _ in range(5)])

    filtered_data = filter_temperatures(raw_readings)

    # Output a summary of the processing result to verify execution without interactive prompts
    print(f"Processed {len(filtered_data)} valid temperature readings out of {len(raw_readings)}.")
    
    if len(filtered_data) > 0:
        avg_temp = statistics.mean(filtered_data)
        min_temp = min(filtered_data)
        max_temp = max(filtered_data)
        print(f"Average Temperature (°C): {avg_temp:.2f}")
        print(f"Minimum Valid Temperature (°C): {min_temp:.2f}")
        print(f"Maximum Valid Temperature (°C): {max_temp:.2f}")
    else:
        print("No valid temperature readings found.")