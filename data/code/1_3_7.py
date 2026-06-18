import heapq

def find_outlier_measurements(entries: list[float], min_val: float = 50, max_val: float = 200) -> list[int]:
    """
    Efficiently identifies indices of weight entries outside the acceptable range.
    
    This function uses a heap to maintain elements in descending order for efficient 
    retrieval of outliers when combined with sorting logic or direct iteration if full scan is needed.
    For this specific task (range check), a single pass O(n) approach without extra data structures 
    like heaps is optimal and most Pythonic, but we structure the solution to handle large datasets efficiently 
    by processing in batches if necessary or leveraging vectorization concepts implicitly through clear logic.
    
    However, since standard list comprehensions are highly optimized C-level loops in Python, 
    a direct iteration with early filtering (though full scan is needed here) offers the best balance of readability and efficiency for this specific range check compared to complex heap operations which would add overhead without benefit for simple min/max checks.
    
    We will use a generator expression fed into list() for memory efficiency if datasets are massive, 
    though Python's slicing or comprehensions on large lists is generally efficient enough given the constraints.
    
    Args:
        entries (list[float]): List of weight measurements.
        min_val (float): Minimum acceptable value.
        max_val (float): Maximum acceptable value.
        
    Returns:
        list[int]: Sorted list of indices where weights are outside [min_val, max_val].
    """
    
    # Single pass O(n) iteration to find outliers
    outlier_indices = []
    
    for idx, weight in enumerate(entries):
        if not (min_val <= weight <= max_val):
            outlier_indices.append(idx)
            
    return sorted(outlier_indices)

if __name__ == '__main__':
    # Hard-coded sample values representing a large dataset scenario
    weights = [50.1, 49.8, 200.5, 60.0, 300.0, 70.0, 40.0, 150.0]
    
    # Identify measurements outside range (default: 50 to 200)
    outliers = find_outlier_measurements(weights)
    
    print(f"Indices of weights outside the acceptable range [50, 200]: {outliers}")