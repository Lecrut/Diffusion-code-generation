import statistics

def find_out_of_range_weights(weight_entries: list[float], min_limit: float = 50, max_limit: float = 200) -> dict[str, int]:
    """
    Process a large dataset of weight entries to identify measurements outside the acceptable range.
    
    Args:
        weight_entries (list): List of weights in kilograms.
        min_limit (float): Lower bound of acceptable range (inclusive).
        max_limit (float): Upper bound of acceptable range (exclusive for efficiency check logic, but effectively inclusive boundaries here as per standard "between" unless specified otherwise; adjusted to be strict inequality inside: value < 50 or value > 200). Note: Based on prompt "between 50 and 200", we treat this as [50, 200]. So out of range is (<50) OR (>200).
    
    Returns:
        dict: Keys are category names ('underweight', 'overweight'), values are counts. Also includes total processed and list of offending entries for detailed view if needed (though prompt asks to identify, usually implying a count or summary; here we return stats + sample data structure for efficiency demonstration).
    """
    
    # Using single pass iteration for O(n) time complexity instead of filtering first then processing second.
    underweight_count = 0
    overweight_count = 0
    
    out_of_range_data = []

    for entry in weight_entries:
        if entry < min_limit or entry > max_limit:
            # Check specifically which range to categorize clearly, though prompt implies "outside" is the main flag.
            # Let's split for better utility without extra function calls per item (which could be micro-optimized).
            # However, simple boolean logic `if` already separates them in one pass branch if we structure it right? 
            # Actually: `val < min or val > max`. If true, then check which.
            
            is_under = entry < min_limit
            is_over = entry > max_limit
            
            if not is_under and is_over:
                overweight_count += 1
                out_of_range_data.append(entry) 
            else: # One must be the only reason since it's OR of two disjoint events (min=50, max=200 are distinct unless they cross which they don't here). Wait.
                if is_under and not is_over:
                    underweight_count += 1
                    out_of_range_data.append(entry)

if __name__ == '__main__':
    pass
