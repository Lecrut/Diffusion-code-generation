import statistics

def main():
    # Sample volume measurements as hard-coded values to ensure no user input is required
    sample_volumes = [10, 25, 30, 45]
    
    print("Sample Volume Measurements:")
    for i, vol in enumerate(sample_volumes):
        print(f"Volume {i + 1}: {vol}")

    total_volume = sum(sample_volumes)
    average_volume = statistics.mean(sample_volumes)

    print("\nCalculated Results:")
    print(f"Total Volume: {total_volume}")
    print(f"Average Volume: {average_volume:.2f}")

if __name__ == '__main__':
    main()