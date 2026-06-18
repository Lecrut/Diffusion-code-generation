"""
Module demonstrating efficient string construction using list comprehension 
and str.join() method.

This module illustrates how to avoid repeated function calls (like + concatenation)
which occur in a loop, by pre-computing parts and then joining them once.
Optimization: Using ''.join(list_of_parts) is generally faster than iterative '+ ' concatenation 
because the latter performs O(n^2) string allocations and copies due to immutability of strings 
in Python, whereas join() creates one list of small objects first (O(n)) and then allocates 
a single large output buffer once.
"""

def build_sentence_optimized(sizes: list[int], units: list[str]) -> str:
    """
    Builds a descriptive sentence given the sizes and unit types for various elements.

    Args:
        sizes: List of integer sizes (e.g., width, height).
        units: List of string descriptions corresponding to each size.

    Returns:
        A single formatted string constructed efficiently using list comprehension 
        and str.join().
    """
    # We construct a generator expression inside the join call for memory efficiency if needed,
    # but since inputs are already lists, we use standard list comprehensions here.
    
    parts = [f"The {unit} is {size}" for size in sizes for unit in units] 
    return ''.join(parts)

def build_sentence_optimized_join(sizes: list[int], labels: dict[str, str]) -> str:
    """
    Alternative optimized version using explicit join on a constructed part list.

    Args:
        sizes: List of integer values representing the size attributes (e.g., 'width', 'height').
        labels: A dictionary mapping index keys to descriptive strings for each attribute name 
                and value pair, e.g., {0: "large", 1: "fast"}.

    Returns:
        A formatted string where each combination of dimension key-value is joined together.
    
    Optimization Note:
        Instead of doing `sentence = sentence + new_piece` inside a loop (which involves 
        growing an internal array multiple times), we build a list of small strings first,
        and then apply str.join(). This minimizes string copying overhead to O(N) rather than O(N^2).
    """
    # Using zip for efficient pairing of size keys with their descriptions.
    dimension_info = [f"Dimension {key}: {val}" for key in labels.keys()]

if __name__ == '__main__':
    pass
