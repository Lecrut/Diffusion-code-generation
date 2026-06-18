def compare_temperatures(t1: float, t2: float) -> str | None:
    """Yields a string describing the temperature difference between two values."""
    diff = abs(t1 - t2)
    
    if not diff or (diff < 0.5):
        print("T1 and T2 are essentially equal")
    else:
        result_direction = "warmer" if t1 > t2 else "cooler"
        
        # Format the difference to two decimal places for precision
        formatted_diff = f"{diff:.2f}"
    
    message = f"T{1} is {result_direction} by {formatted_diff} degrees."
    yield message

if __name__ == '__main__':
    temp_a = 75.0
    temp_b = 82.3
    
    for result in compare_temperatures(temp_a, temp_b):
        print(result)