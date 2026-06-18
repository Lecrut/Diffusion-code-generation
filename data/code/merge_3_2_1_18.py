def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements efficiently.
    
    Args:
        volumes (list[float]): A list containing numeric volume values.
        
    Returns:
        float or None: The average volume if input is valid, otherwise returns 0 for empty lists 
                       and raises ValueError for non-numeric data types mixed in without proper handling.
                       
    For maximum efficiency as per the task requirement using built-in functions (sum) which are implemented 
    efficiently under the hood via C loops rather than interpreted Python list comprehensions when performance is critical,
    though a generator expression within sum would be more memory efficient for very large lists if we were strictly optimizing space.
    However, since standard practice favors speed with built-ins and 'sum' on a direct iterator or list comprehension 
    are the two main paths, let's use 'sum' directly which is highly optimized in CPython.
    
    Note: To satisfy "using list comprehensions OR built-in functions", we will prioritize the built-in sum for raw arithmetic efficiency,
    but to strictly demonstrate usage of a comprehension pattern as hinted by alternative interpretations of optimization goals 
    (like mapping types first), here's a hybrid approach that is robust and efficient.

    Actually, re-reading: "using list comprehensions or built-in functions". The most direct optimized mean calculation in Python 
    without external libraries relies heavily on sum(). A generator expression inside sum() saves memory compared to a full list comprehension.
    
    Let's stick to the simplest highly optimized form using sum and iteration over the input which is efficient enough for typical use cases,
    but we can wrap it with validation if needed. Since no error handling strategy was asked beyond returning 0 or similar (implied by task constraints), 
    let's assume valid numeric floats are passed as per sample block requirement.

    Final Decision: Use `sum(volumes) / len(volumes)` which leverages the C-optimized sum implementation of Python for best speed/memory balance here,
    avoiding explicit loops while meeting the spirit of 'built-in functions'. If strict list comprehension usage was mandated instead, 
    we could do `(sum(x for x in volumes))` (generator - slightly slower than built-in loop but avoids creating intermediate list) or `list(map...)`.
    
    Given "maximum efficiency", raw sum on iterable is best. But to explicitly show the requested pattern capability without compromising speed too much:

    We'll provide a solution that uses standard arithmetic which relies heavily on optimized internal C code for 'sum'. 
    This satisfies the constraint of using built-ins efficiently.

    However, if we MUST use list comprehension as per strict reading of "using ... OR ...":
    Let's do it cleanly with sum over mapped float values just in case inputs might be strings (though samples imply numbers).
    
    Actually, simplest and fastest valid interpretation:
    """
    # Using built-in functions for maximum efficiency. 
    # 'sum' is implemented in C and handles the accumulation very efficiently.
    if not volumes or all(not isinstance(v, (int, float)) for v in volumes):
        return 0
        
    total = sum(float(x) for x in volumes)
    count = len(volumes)
    
    # If we strictly want to force a list comprehension creation which might be slightly slower due to object creation overhead 
    # than generator or raw iteration, but the prompt says 'OR', so built-in sum is acceptable.
    # To ensure robustness against non-float inputs in generic cases:
    
    if total == 0 and count > 0:
        return 0.0

    return float(total) / float(count)

if __name__ == '__main__':
    sample_volumes = [12, 45, 36, 78, 90]
    
    # Calculate the average volume using the optimized function
    avg_vol = calculate_average_volume(sample_volumes)

    print(f"Volume Measurements: {sample_volumes}")
    print(f"Calculated Average Volume: {avg_vol}")