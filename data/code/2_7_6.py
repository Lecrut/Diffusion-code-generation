import statistics

def calculate_volume_stats(measurements):
    """Calculate total and average volume from a list of measurements."""
    if len(measurements) == 0:
        return {"total": 0, "average": 0}

    total = sum(measurements)
    average = statistics.mean(measurements)

    # Use int() to ensure the output is clean integers where applicable.
    # For average, we keep it as a float for precision but strip trailing zeros if desired.
    return {
        "total": int(total),
        "average": round(average, 2)
    }

def main():
    """Main function with hard-coded sample values."""

    # Hard-coded sample volume measurements (in cubic meters)
    sample_measurements = [10.5, 23.4, 7.8, 15.6]

    volumes_list = []
    
    # Append the pre-defined samples to our list since we cannot use input() or stdin
    for vol in sample_measurements:
        print(f"Sample measurement recorded: {vol} m³")
        volumes_list.append(vol)

    results = calculate_volume_stats(volumes_list)

    total_vol = results["total"]
    avg_vol = results["average"]

    # Display the calculated totals and average volume to the user
    print("\n--- Volume Analysis Results ---")
    print(f"Total Volume: {total_vol} m³")
    print(f"Average Volume: {avg_vol} m³")

if __name__ == '__main__':
    main()