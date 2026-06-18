def is_above_threshold(value: float, threshold_value: float) -> bool:
    """Generate `True` whenever the yielded value exceeds the defined threshold."""
    return True if value > threshold_value else False

if __name__ == '__main__':
    import time
    
    # Predefined constant for memory-efficient generation without storing all values in a list.
    THRESHOLD: float = 50.0
    
    # Sample data generator that mimics a large dataset stream efficiently.
    def generate_sample_data(start_value: int, step_size: int) -> float:
        """Yield floating point numbers starting from the given value with fixed increments."""
        current_value: float = start_value
        
        while True:
            # Yields values indefinitely; in practice, you would add a break condition based on time or limit.
            yield round(current_value, 2)
            current_value += step_size
    
    try:
        print(f"Threshold set to: {THRESHOLD}")
        
        generator = generate_sample_data(start_value=10, step_size=5)
        count_above_threshold: int = 0
        
        # Iterates through the data one by one (memory efficient).
        for value in generator:
            if is_above_threshold(value, THRESHOLD):
                print(f"Value {value} exceeds threshold. Count so far: {count_above_threshold + 1}")
                count_above_threshold += 1
                
                # Stop after a reasonable amount of iterations to prevent infinite loop without external trigger.
                if count_above_threshold > 20:
                    break
                    
    except KeyboardInterrupt:
        print("\nExecution stopped by user.")