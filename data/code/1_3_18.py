import json

def identify_outliers(weight_data: list[float], min_limit: float = 50, max_limit: float = 200) -> list[dict]:
    """
    Processes a dataset of weight entries and identifies measurements outside the acceptable range.
    
    Args:
        weight_data (list[float]): A list of numerical values representing weights in kilograms.
        min_limit (float): The lower bound of the acceptable range (inclusive).
        max_limit (float): The upper bound of the acceptable range (inclusive).
        
    Returns:
        list[dict]: A list of dictionaries containing details about each outlier measurement.
                   Each dictionary includes 'index', 'value', and a descriptive message.
    
    Time Complexity: O(n), where n is the number of entries in weight_data.
    Space Complexity: O(k), where k is the number of outliers found (to store results).
    """
    outliers = []

    for index, value in enumerate(weight_data):
        if not isinstance(value, (int, float)):
            # Skip non-numeric values to ensure algorithm efficiency and robustness
            continue
            
        if value < min_limit or value > max_limit:
            outlier_info = {
                'index': index,
                'value': value,
                'message': f"Measurement out of range [{min_limit}, {max_limit}]: {value} kg detected."
            }
            outliers.append(outlier_info)

    return outliers

if __name__ == '__main__':
    # Hard-coded sample dataset simulating weight entries in kilograms.
    # Includes valid values (50-200), boundary values, and out-of-range values to test logic.
    SAMPLE_WEIGHTS = [48, 198, 210, 75, -5, 60, 300, 150]

    # Process the dataset with predefined limits (50kg to 200kg)
    identified_outliers = identify_outliers(SAMPLE_WEIGHTS, min_limit=50, max_limit=200)

    if not identified_outliers:
        print("No weight measurements outside the acceptable range were found.")
    else:
        # Output results as a JSON string for clear structure without console prompt dependencies
        result_json = json.dumps(identified_outliers, indent=4)
        print(result_json)