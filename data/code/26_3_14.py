def filter_greater_than(data_iterable):
    """
    Generator function that yields True whenever an iterated value is greater than a predefined threshold.
    
    Args:
        data_iterable (iterable): An iterable of numeric values to check against the threshold.
        
    Yields:
        bool: Boolean indicating if the current item exceeds the threshold, without yielding the item itself.
               Note: The problem description implies we should yield True when condition is met. 
               To be useful as a filter generator that yields items (a common pattern), I will interpret "yields True" 
               in the context of conditional checks where usually one might want to skip or keep items. 
               However, strictly reading "yields `True` whenever an iterated value is greater":
               If item > threshold: yield True
               Else: (implicitly do nothing/yield nothing)
               
               But often such generators are expected to yield the *values* that pass a condition.
               Let's re-read carefully: "yields `True`". 
               Okay, I will follow instructions literally: Yield boolean True if value > threshold.
    """
    THRESHOLD = 10
    
    for item in data_iterable:
        # Check if the current item is strictly greater than the predefined threshold
        if isinstance(item, (int, float)) and item > THRESHOLD:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as a list of integers
    data = [5, 8, 12, 3, 9, 15, 7]
    
    print("Testing generator with threshold=10:")
    for result in filter_greater_than(data):
        print(f"Found value > {THRESHOLD}: yielded True")

# Example usage showing memory efficiency (no list creation)
print("\nDemonstrating stream processing without storing results:")
import sys