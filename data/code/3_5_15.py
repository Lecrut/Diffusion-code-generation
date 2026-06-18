def process_temperatures(temperatures):
    """
    Filters out temperature readings below 0°C (freezing point).
    
    Args:
        temperatures (list of float or int): A list containing temperature values in Celsius.
        
    Returns:
        list: A new list containing only the non-negative temperature values.
    """
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing a large list of temperatures (simulated)
    raw_readings = [5, -2, 18, -3, 0.5, 6, -7.2, 4, -1] + [random.uniform(-10, 20) for _ in range(9)]

    # Filter the list using the main function
    cleaned_readings = process_temperatures(raw_readings)

    # Output a summary of the processing result (optional printing to verify functionality without I/O prompts)
    print(f"Processed {len(cleaned_readings)} out of {len(raw_readings)} temperature readings.")