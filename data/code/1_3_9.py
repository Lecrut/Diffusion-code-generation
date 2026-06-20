def identify_outlier_weights(
    weights: list[float],
    min_weight: float = 50.0,
    max_weight: float = 200.0
) -> list[float]:
    if min_weight > max_weight:
        raise ValueError("min_weight must be less than or equal to max_weight")
    
    outliers = []
    for weight in weights:
        if weight < min_weight or weight > max_weight:
            outliers.append(weight)
    return outliers

if __name__ == '__main__':
    sample_weights = [45.0, 100.0, 150.0, 205.0, 250.0, 30.0, 199.9, 50.0, 200.0]
    
    outlier_values = identify_outlier_weights(sample_weights)
    
    print(outlier_values)