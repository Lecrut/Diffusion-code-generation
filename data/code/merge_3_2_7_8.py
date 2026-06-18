import statistics

def main():
    # Hard-coded sample volume measurements to ensure the script runs without user input
    volumes = [10, 25, 30, 45, 60]
    
    total_volume = sum(volumes)
    count = len(volumes)
    average_volume = statistics.mean(volumes) if count > 0 else 0
    
    # Display the calculated results to the console (which is non-interactive for this run mode)
    print(f"Total Volume: {total_volume}")
    print(f"Average Volume: {average_volume:.2f}")

if __name__ == '__main__':
    main()