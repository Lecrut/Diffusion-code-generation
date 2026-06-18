import statistics

def calculate_volumes():
    """Calculates total and average volume from a list of measurements."""
    volumes = [10, 25, 30]  # Hard-coded sample values
    
    try:
        if not isinstance(volumes, (list, tuple)):
            raise ValueError("Volume data must be in the form of a list or tuple.")
            
        total_volume = sum(volumes)
        
        if len(volumes) > 0:
            average_volume = statistics.mean(volumes)
        else:
            average_volume = None
            
    except Exception as e:
        print(f"Error calculating volumes due to invalid data format or value type: {e}")

def display_results(total, average):
    """Displays the calculated total and average volume."""
    if isinstance(average, float) or (isinstance(average, int)):
        avg_str = str(round(average))
    else: 
        avg_str = "N/A"
    
    print(f"\nTotal Volume: {total}")
    print(f"Average Volume: {avg_str}")

if __name__ == '__main__':
    calculate_volumes()