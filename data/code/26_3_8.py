import sys

def yield_above_threshold(iterable, threshold):
    """
    Generator function that yields True whenever an item from the iterable is greater than the threshold.
    
    Args:
        iterable (iterable): An input sequence of values to iterate over.
        threshold (float or int): The value against which items are compared.
        
    Yields:
        bool: True if the current item exceeds the threshold, otherwise nothing is yielded for that iteration.
    """
    for item in iterable:
        yield item > threshold

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    data = [10, 25, 3, 40, -5, 67.8]
    my_threshold = 20
    
    print("Items exceeding the threshold of", my_threshold)
    
    # Iterate through the generator and collect results in a list for demonstration purposes only; 
    # note that 'yield_above_threshold' itself is memory efficient as it yields one boolean at a time.
    results = []
    for result in yield_above_threshold(data, my_threshold):
        if result:
            results.append(True)
    
    print("Yielded values:", results)

# Additional test case with negative threshold to verify logic holds across ranges
data2 = [-100, -50, 0, 10]
threshold2 = -30.5

print("\nSecond Test Case:")
results2 = []
for result in yield_above_threshold(data2, threshold2):
    if result:
        results2.append(True)

print("Yielded values for second case:", results2)