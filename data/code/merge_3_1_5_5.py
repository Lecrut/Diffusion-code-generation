def extract_weights(record):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Parameters:
        record (any): The data object, expected to be either a dict or float/int/numeric value.
        
    Returns:
        list[float]: A list of extracted numeric weights from the entire structure.
    """
    results = []
    
    if isinstance(record, dict):
        for key, value in record.items():
            # Recursively process values that are still dictionaries or other valid types to add
            results.extend(extract_weights(value))
    elif isinstance(record, (int, float)):
        results.append(float(record))

    return results

if __name__ == '__main__':
    pass
