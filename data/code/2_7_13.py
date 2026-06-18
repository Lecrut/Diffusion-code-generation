import sys

def calculate_volumes():
    """Calculates total and average volume from a list of measurements."""
    volumes = [10, 25, 30]  # Hard-coded sample values
    
    try:
        total_volume = sum(volumes)
        
        if len(volumes) > 0:
            avg_volume = total_volume / len(volumes)
            
            print(f"Total Volume: {total_volume}")
            print(f"Average Volume: {avg_volume:.2f}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")

if __name__ == '__main__':
    calculate_volumes()