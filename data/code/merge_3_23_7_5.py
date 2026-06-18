import sys
from typing import Set, Any

def calculate_set_operations(set_x: Set[Any], set_y: Set[Any]) -> dict[str, int]:
    """
    Calculates intersection and union of two sets and returns their sizes along with the difference.
    
    Args:
        set_x (Set): First input set.
        set_y (Set): Second input set.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'difference'.
    """
    intersection = set_x.intersection(set_y)
    union_set = set_x.union(set_y)
    
    return {
        "intersection_size": len(intersection),
        "union_size": len(union_set),
        "difference": abs(len(union_set) - len(intersection))
    }

def main():
    # Hard-coded sample values for testing, running without user input or files.
    set_x: Set[int] = {10, 20, 30, 40}
    set_y: Set[int] = {30, 40, 50, 60}

    result = calculate_set_operations(set_x, set_y)
    
    print(f"Intersection size: {result['intersection_size']}")
    print(f"Union size: {result['union_size']}")
    print(f"Difference in sizes: {result['difference']}")

if __name__ == "__main__":
    main()