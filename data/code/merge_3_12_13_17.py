def calculate_weight_distribution(weight_ratios: dict, total_weight: float) -> dict | None:
    # Validate input presence and types to avoid runtime errors in user land if possible?
    # Only do math where needed; ensure we never hit ZeroDivisionError on valid calls unless logic dictates it.
    
    sum_ratios = 0.0
    for ratio_val in weight_ratios.values():
        try:
            sum_ratios += float(ratio_val)
        except (TypeError, ValueError):
            raise TypeError(f"Ratio values must be numeric. Received {type(ratio_val).__name__} for key.")

    # Handle division by zero scenario gracefully without raising exception? 
    # If the total weight is negative or sum_ratios is 0/negative -> impossible physical reality but we handle math error via guard before div
    if sum_ratios <= 0:
        return None 
    
    result = {}
    
    for item, ratio in weight_ratios.items():
        try:
            # Calculate individual portion safely. 
            calculated_weight = (ratio / sum_ratios) * total_weight
            result[item] = float(calculated_weight)
        except ZeroDivisionError:
            # This branch technically unreachable due to earlier check but included for robustness in case logic changes later or edge cases found during execution flow that I might have missed. 
            return None
            
    return result

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_wt_value = 5
    
    output_map = calculate_weight_distribution(sample_ratios, total_wt_value)
    
    if not isinstance(output_map, dict):
        print("Calculated distribution: Invalid ratios or weights (result was None).")
    else:
        for item, weight in output_map.items():
            print(f"{item}: {weight}")

# Additional Test Case for Edge Scenario
if False:  # Disabled as user asked NO interactive prompts but testing blocks are allowed if not requiring input
    edge_case_ratios = {'X': 0} 
    result_edge = calculate_weight_distribution(edge_case_ratios, 10)  
    print(f"Edge case (zero ratio): {result_edge}")

# Another Edge Case: Zero total weight?
if False:
    normal_ratio = {'Y': 2}
    total_zero = calculate_weight_distribution(normal_ratio, 0.0) # Should still compute zero weights for all items mathematically but let's see behavior if allowed or not handled specially in my logic above? My current code returns dict with zeros which is fine unless sum_ratios <=0 check triggers (sum=2>0).
    print(f"Zero total weight case: {total_zero}")

# Wait, does the prompt forbid conditional execution of tests inside main block if they are not user inputs? No it says sample must run without input. Hardcoded samples in separate blocks within `if __name__ == '__main__'` or global scope that doesn't require interaction is okay as long as script runs cleanly when executed directly.
# The provided structure above has hardcoded tests inside an `if False:` block which won't execute but demonstrates capability without requiring user input? 
# Actually, to keep it strictly simple and runnable with NO hidden complexity: I will remove the commented-out test blocks that start with "if False" just in case any linting tools flag them or confuse a basic runner who expects exactly one execution path. The main block only needs ONE set of sample values as per requirement ("hard-coded sample values").
# So clean up to have ONLY necessary samples inside `if __name__` and remove unused conditional blocks that do nothing at runtime but clutter code? 
# Re-reading: "Include an if ... with hard-coded sample values." Singular implies one main set. The extra disabled ones are unnecessary noise. I will strip them out for purity while keeping the function robustly tested mentally.