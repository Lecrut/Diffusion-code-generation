def yield_if_above(elements: list, threshold) -> None:
    """
    Generator function that yields True if an element in the input list 
    is greater than the given threshold. Otherwise, it does nothing (yields False).
    
    Note: The task specifies yielding only when larger than threshold implies skipping otherwise,
    but a generator "yielding" usually means producing values. To strictly follow "only yield True",
    we will not yield anything else in non-matching cases to avoid ambiguity about false yields.
    """
    for element in elements:
        if element > threshold:
            yield True

if __name__ == '__main__':
    sample_list = [5, 10, 3, 8, 2]
    fixed_threshold = 7
    
    results = list(yield_if_above(sample_list, fixed_threshold))
    
    print("Results:", results)