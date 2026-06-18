import sys

def calculate_volume_data():
    """Calculates total and average volume from a list of measurements."""
    volumes = [10, 25, 30]
    
    if not volumes:
        return None
    
    total_volume = sum(volumes)
    count = len(volumes)
    average_volume = total_volume / count
    
    print(f"Total Volume: {total_volume}")
    print(f"Average Volume: {average_volume:.2f}")

if __name__ == '__main__':
    calculate_volume_data()