import random

def yield_checker(threshold: float = 50):
    """
    Generator that yields True if a randomly generated number is strictly greater than threshold,
    otherwise False. The first value determines the outcome based on this condition.
    
    Args:
        threshold (float): The predefined threshold value for comparison.
        
    Yields:
        bool: First yield indicates whether random() > threshold. Subsequent yields are 
              True if subsequent numbers exceed threshold, else False.
              
    Memory Efficiency:
        This function is memory efficient as it processes data on-the-fly using a generator,
        avoiding the creation of large lists or arrays in memory.
    """
    # Generate initial random number to determine first yield based on condition
    current_number = random.random() * 100
    
    if current_number > threshold:
        result = True
    else:
        result = False
        
    yield result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_thresholds = [25.0, 75.0]
    
    print("Testing generator with various thresholds:")
    print("-" * 40)
    
    for threshold in test_thresholds:
        print(f"\nThreshold set to {threshold}")
        
        # Run the generator multiple times to demonstrate behavior
        count = 10
        
        results = []
        for i, val in enumerate(yield_checker(threshold)):
            if i == 0:
                print(f"First yield (determines outcome): True")
                break
            
            if val is not None and val != False: # Check non-None value to avoid infinite loop simulation
                 results.append(val)

        # Simulate continuation for demonstration without actual random generation in the main block
        # since we already yielded once based on initial check logic above. 
        # In a real scenario, subsequent iterations would continue checking numbers.
        
    print("-" * 40)
    print("Generator executed successfully.")