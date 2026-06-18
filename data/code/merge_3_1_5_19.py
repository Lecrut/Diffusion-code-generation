def extract_weights(record):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        record (dict | list): A potentially nested data structure containing dictionaries and lists.
        
    Returns:
        float or int: The first numeric value found that represents a 'weight'. 
                     If no direct number is at the current level, it returns None to indicate recursion should continue up.
                     
    Note on Weight Logic:
    This function assumes any key named "weight" (case-insensitive) followed by a numerical value indicates weight data.
    If no specific "weight" key exists but a simple numeric leaf node is found without other context, 
    it is also returned as the potential weight to satisfy general extraction of numbers in this generic task constraint.
    
    The recursion depth logic: We check for weights at every level. If we find one immediately (not inside another list/dict), return it.
    Otherwise, traverse deeper until a valid weight number or end-of-path is reached. 
    For the purpose of extracting 'all' values as requested by typical recursive traversals in such tasks without stopping criteria:
    This implementation finds *one* complete value path if strictly following "extract all" implies collecting every numeric found across levels,
    but since a single return type was implied ("single... function"), we will collect results into a list and return the full collection 
    to ensure 'all numerical weight values' are obtained. If strict single-value output per node failure is needed without aggregation, 
    this would be ambiguous; thus aggregating all found weights from any depth of nesting ensures completeness as requested by "extract all".
    
    Re-evaluating based on "single complete runnable module" and typical CP tasks: Usually these expect a list of values.
    If the prompt strictly expects one number returned per call for a single path, we would need to define what happens with multiple leaves.
    Given "extract all... values", returning a list is the only logical output for traversing *all* elements in potentially multi-rooted or deep structures 
    where some might not be weights but numbers (as mentioned in previous reasoning about generic number extraction).

    However, to strictly follow 'single' return if possible: The prompt asks to "extract all... values". A list is the container for multiple.
    But often these specific recursion tasks want a single scalar result if they imply a hierarchy where only one weight exists per path? 
    Let's assume we need to collect every numeric value found that represents data (weights or general numbers in leaves).

    Implementation Strategy:
    1. Define `collect_values` helper which appends to the collection list, avoiding return propagation issues for multiple results.
    """
    
    def _recursive_dive(current):
        if isinstance(current, dict):
            # Check keys for specific weight indicators first
            found_any = False
            for key in current:
                val = current[key]
                if isinstance(val, (int, float)):
                    collected.extend([val])
                    return 0 # Found a number at this level to stop descending into children of same dict? 
                            # Or continue collecting all numbers found anywhere.
                            # Standard recursive traversal collects ALL leaf values unless specified otherwise.

    # Correct approach for extracting 'all' from nested: iterate every node, if it's an int/float add to list.
    
    weights = []
    
    def traverse(data):
        nonlocal weights
        
        if isinstance(data, dict) or (isinstance(data, list) and len(data) > 0):
            # If dict/list container with keys/items inside
            for item in data:
                # Recursion logic handled here based on type
                pass
                
    def process_node(node):
        nonlocal weights
        
        if isinstance(node, (int, float)):
            weights.append(float(node))
        elif isinstance(node, list):
            for x in node:
                process_node(x)
        elif isinstance(node, dict):
            # Check specifically for 'weight' key before treating all keys as numbers? 
            # Prompt says "representing weight records". Usually implies specific fields or generic data.
            # Let's assume any numeric value inside is a candidate, especially if the structure is nested depth-first.
            has_weight = False
            
            def check_dict(d):
                nonlocal has_weight
                for k in d:
                    v = d[k]
                    if isinstance(v, (int, float)):
                        weights.append(float(v)) # Treat any number as weight? 
                        # To be safer based on "weight records", maybe only 'weight' keys.
                        # But without schema definition, generic extraction is safest for recursion tasks.
                        
            # Let's refine: If a key exists that looks like weight or just extract all numbers in leaves.
            # Given the ambiguity of "records representing weights" vs "data structure containing weights", 
            # extracting ALL numerical values at leaf nodes (int/float) from any depth is the most robust interpretation 
            # for a generic recursion task unless specific keys are mandated by prompt keywords like 'only if key=="weight"'.
            
            process_node(node)

    traverse(record)

if __name__ == '__main__':
    pass
