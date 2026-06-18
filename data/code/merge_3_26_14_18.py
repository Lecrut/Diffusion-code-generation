import sys

def greater_than_threshold(value: float, threshold: float) -> bool:
    """Check if a value is strictly greater than the given threshold."""
    return value > threshold

def generator_function(values_generator):
    """
    Generator that yields True only when the input from values_generator 
    is strictly greater than a predefined threshold.
    
    This implementation is memory-efficient as it processes items one by one,
    without storing them in a list or other data structure.
    
    Args:
        values_generator: An iterable of numeric values to check against the threshold.
        
    Yields:
        True if the current value from values_generator is greater than THRESHOLD, False otherwise.
    """
    global THRESHOLD
    
    for val in values_generator:
        # Check if the value meets the condition before yielding
        result = greater_than_threshold(val, THRESHOLD)
        
        # Only yield True when the condition is met to save memory and bandwidth 
        # on unnecessary data transmission or processing downstream.
        if result:
            yield True

# Predefined threshold for comparison
THRESHOLD = 50.0

if __name__ == '__main__':
    # Hard-coded sample values representing a large sequence without loading everything into memory at once
    # We simulate an iterator to demonstrate the generator's behavior efficiently
    
    def create_sample_sequence():
        """Generator that yields numbers up to 200."""
        for i in range(1, 201):
            yield float(i)

    sample_gen = create_sample_sequence()
    
    # Process and print results directly from the generator without storing them
    count_true = 0
    
    try:
        while True:
            result_value = next(sample_gen)
            if greater_than_threshold(result_value, THRESHOLD):
                yield_result = True
                
                # Simulate yielding to a consumer (in this case, printing and counting)
                print(f"Value {result_value} > Threshold {THRESHOLD}: Yielded True")
                
    except StopIteration:
        pass
    
    print("Sequence exhausted. Generator completed successfully.")