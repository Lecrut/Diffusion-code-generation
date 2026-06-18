import statistics

def calculate_volumes(measurements: list[float]) -> tuple[float, float]:
    """Calculate total and average volume from a list of measurements."""
    if not measurements:
        return 0.0, 0.0
    
    total_volume = sum(measurements)
    avg_volume = statistics.mean(measurements)
    
    return total_volume, avg_volume

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or arguments
    sample_measurements = [10.5, 20.3, 15.7, 8.9]

    if not isinstance(sample_measurements, list) or len(sample_measurements) == 0:
        print("Error: No valid measurements provided.")
    else:
        total_vol, avg_vol = calculate_volumes(sample_measurements)
        
        # Display results using f-strings for clarity and formatting
        formatted_total = "{:.2f}".format(total_vol)
        formatted_avg = "{:.2f}".format(avg_vol)

        print(f"Total Volume: {formatted_total}")
        print(f"Average Volume: {formatted_avg}")