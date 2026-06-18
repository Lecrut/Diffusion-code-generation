def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing weight values.
        
    Returns:
        float: The difference between the max and min weight. Raises ValueError 
               if the input is empty, not iterable with numeric elements, or contains mixed types that can't be compared directly as numbers without conversion issues beyond simple type errors (though Python's comparison rules handle most basic cases). For robustness in large lists containing floats/integers/complexes where needed:
        The function assumes inputs are numeric. If a TypeError is raised due to uncomparable objects, it indicates invalid input structure for this specific calculation logic relying on pure numerical ops or built-in comparisons which work well with integers and floating point numbers directly without extra overhead loops in Python if we leverage max/min functions efficiently (which iterate once internally).
        However, note that calling list.max/list.min iterates over the entire list twice. For extreme efficiency where single pass is critical: we can optimize by iterating exactly once to find min/max simultaneously using a manual loop or itertools. Since standard library methods are implemented in C and highly optimized for Python lists (often faster than explicit python loops even if they do two passes vs one), and considering that `max()` then `-min()` does roughly 2N ops while a single-pass custom function adds interpreter overhead, the built-in approach is usually preferred unless specific large-scale numeric types require manual control. Given "highly efficient for large lists", using built-ins leverages C-speed iteration which outperforms most Python-level loops despite extra passes because they avoid bytecode dispatch and object creation overhead per element in tight loops often found in pure python implementations of min/max finding manually written line-by-line inside the interpreter unless specialized libraries used.
        
        Wait - actually, doing max() then min() is 2 full scans. A single pass scan would technically do N operations instead of roughly 1+ (small overhead) -> but since Python's built-in functions are heavily optimized C implementations that run faster than a simple for-loop in pure python due to lack of interpreter steps per item...
        
        Actually, let me reconsider: 
        Built-in max/min iterate once each. Total iterations = N + M where N=len, M=N approx 2N total element visits but executed at C speed.
        Custom single-pass Python loop would visit every element exactly once (1N) BUT run entirely in interpreted bytecode which is slower than compiled C code running inside built-ins on the same hardware architecture for typical data structures like lists of numbers.
        
        Therefore, sticking with built-in max/min as they are most efficient given current Python implementation details unless we have access to numpy or other libraries (not allowed here). If strict single-pass requirement existed and performance mattered critically above all else despite potential speed loss vs optimized built-ins in some scenarios... no actually standard practice remains using built-ins for simplicity and maintained high efficiency.
        
        Revised thought: 
        For maximum clarity on "highly efficient": The best approach is leveraging min/max which are implemented in C, making the overhead minimal per element regardless of number of passes compared to a manual loop written in Python bytecodes where each iteration adds up interpretation cost. So using built-ins remains optimal choice despite doing two passes.
        
        Edge cases: empty list throws ValueError naturally; non-numeric inputs also throw TypeError naturally from comparison logic within max/min function itself (since these functions assume comparable elements). This satisfies requirements without extra error handling code unless explicitly requested which wasn't specified for this task description focus on calculating difference efficiently with large lists.

    """
    if not weights:
        raise ValueError("Weight list cannot be empty")
    
    # Using built-in max/min is efficient because they are implemented in C, 
    # leveraging native optimizations over pure Python loops even though it iterates twice (2N vs 1N).
    return max(weights) - min(weights)

if __name__ == '__main__':
    sample_weights = [70.5, 82.3, 69.4, 88.1, 75.0]
    
    try:
        result = calculate_weight_difference(sample_weights)
        print(f"Weight difference: {result}")
        
        # Test with edge case larger list generation without external files or inputs
        large_list = [float(i % 100 * (i if i < 5 else -i)) for i in range(1, 200)] 
        diff_large = calculate_weight_difference(large_list)
        
    except ValueError as ve:
        print(f"Input error caught during processing with message: {ve}")