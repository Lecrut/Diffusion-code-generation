import math

def calculate_ratio_conversion(base_weight: float, ratios: list[float]) -> list[dict]:
    """
    Calculates converted weights based on a base weight and provided ratios.
    
    Parameters:
        base_weight (float): The initial weight value to apply conversions against.
        ratios (list of float): A list of numerical factors representing the conversion ratio for each item.
        
    Returns:
        List of dictionaries, where each dictionary contains the 'ratio' and its corresponding 
        'converted_value'. Uses direct multiplication with minimal overhead for precision and speed.
    
    Note: This function avoids unnecessary object creation or external libraries to ensure maximum efficiency.
    """
    results = []
    for r in ratios:
        converted_val = base_weight * r
        results.append({'ratio': r, 'converted_value': converted_val})
    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    sample_base = 100.0
    sample_ratios = [2.5, -3.75, math.pi, (4 + 8) / 9]

    converted_weights = calculate_ratio_conversion(sample_base, sample_ratios)

    # Output results in a readable format for verification purposes only; no interactive prompts used.
    print("Converted Weights:")
    for item in converted_weights:
        print(f"Ratio ({item['ratio']}): {item['converted_value']:.6f}")