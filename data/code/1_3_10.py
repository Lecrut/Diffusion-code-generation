import statistics

def find_outlier_weights(weight_entries: list[float], min_acceptable: float = 50, max_acceptable: float = 200) -> dict[str, any]:
    """
    Identifies weight measurements falling outside the acceptable range.
    
    Args:
        weight_entries (list[float]): List of individual weight measurements.
        min_acceptable (float): Lower bound of the acceptable range.
        max_acceptable (float): Upper bound of the acceptable range.
        
    Returns:
        dict[str, any]: A dictionary containing counts and statistics for outliers.
            Keys include 'outlier_count', 'total_entries', 
            'average_outliers', 'min_outlier', 'max_outlier'.
    """
    # Filter entries that are outside the acceptable range [50, 200]
    outlier_weights = []
    
    for weight in weight_entries:
        if not (min_acceptable <= weight <= max_acceptable):
            outlier_weights.append(weight)

    total_entries = len(weight_entries)
    result = {
        'outlier_count': len(outlier_weights),
        'total_entries': total_entries,
        'percentage_outliers': 0.0 if total_entries == 0 else (len(outlier_weights) / total_entries * 100),
        'average_outliers': statistics.mean(outlier_weights) if outlier_weights else None,
        'min_outlier': min(outlier_weights) if outlier_weights else None,
        'max_outlier': max(outlier_weights) if outlier_weights else None
    }

    return result

if __name__ == '__main__':
    # Hard-coded sample values representing a large dataset simulation
    # Includes valid entries (50-200 kg), low outliers (< 50 kg), and high outliers (> 200 kg)
    sample_data = [60, 75, 180, 45, 90, 300, 120, 40, 150, 210] * 10
    
    # Process the dataset
    analysis_results = find_outlier_weights(sample_data)

    # Output results to console (no file I/O or network access used)
    print("Weight Analysis Report")
    print("=====================")
    print(f"Total Entries Analyzed: {analysis_results['total_entries']}")
    print(f"Outliers Found:        {analysis_results['outlier_count']}")
    
    if analysis_results['percentage_outliers'] is not None:
        print(f"Percentage Outliers:   {analysis_results['percentage_outliers']:.2f}%")

    print("\nOutlier Statistics:")
    if analysis_results['average_outliers']:
        print(f"  Average Weight (kg): {analysis_results['average_outliers']:.2f}")
    
    if analysis_results['min_outlier'] is not None:
        print(f"  Minimum Weight (kg): {analysis_results['min_outlier']}")
        
    if analysis_results['max_outlier'] is not None:
        print(f"  Maximum Weight (kg): {analysis_results['max_outlier']}")