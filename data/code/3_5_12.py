import statistics

def filter_temperatures(temperatures):
    """
    Filters out temperature readings below 0°C from a list of temperatures.
    
    Args:
        temperatures (list[float]): A list of floating-point numbers representing 
                                   temperature readings in degrees Celsius.
        
    Returns:
        list[float]: A new list containing only the non-negative temperature values.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing daily high/low temperatures over a week
    raw_readings = [-5, -2, 3, 18, 4.5, -7, 9, 0, 12, 6]
    
    filtered_data = filter_temperatures(raw_readings)
    
    print("Original readings:", raw_readings)
    print("Filtered temperatures (>= 0°C):", filtered_data)
    
    # Optional: Calculate and display the average of remaining valid temperatures
    if len(filtered_data) > 0:
        avg_temp = statistics.mean(filtered_data)
        print(f"Average temperature of valid readings: {avg_temp:.2f}°C")