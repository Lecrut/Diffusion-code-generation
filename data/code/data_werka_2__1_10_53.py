import numpy as np

def validate_weights(weights):
    if not isinstance(weights, (list, np.ndarray)):
        raise ValueError('Weights must be a list or numpy array.')
    if not all((isinstance(w, (int, float)) for w in weights)):
        raise ValueError('All elements in weights must be numbers.')

def validate_percentage_change(percentage_change):
    if not isinstance(percentage_change, (int, float)):
        raise ValueError('Percentage change must be a number.')

def adjust_weights(weights, percentage_change):
    validate_weights(weights)
    validate_percentage_change(percentage_change)
    
    weights_array = np.array(weights)
    adjusted_weights = weights_array * (1 + percentage_change)
    return adjusted_weights.tolist()

if __name__ == '__main__':
    sample_weights = [65.0, 72.5, 85.3, 90.2]
    percentage_change = -0.05
    new_weights = adjust_weights(sample_weights, percentage_change)
    print(new_weights)