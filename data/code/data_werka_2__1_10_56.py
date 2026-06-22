import numpy as np

class WeightAdjuster:
    def __init__(self, weights):
        if not isinstance(weights, (list, np.ndarray)):
            raise ValueError('Weights must be a list or numpy array.')
        if not all((isinstance(w, (int, float)) for w in weights)):
            raise ValueError('All elements in weights must be numbers.')
        self.weights = np.array(weights)
    
    def apply_percentage_change(self, percentage_change):
        if not isinstance(percentage_change, (int, float)):
            raise ValueError('Percentage change must be a number.')
        return self.weights * (1 + percentage_change)

if __name__ == '__main__':
    sample_weights = [65.3, 72.8, 84.5, 90.2]
    percentage_change_1 = 0.05
    percentage_change_2 = -0.10
    
    weight_adjuster = WeightAdjuster(sample_weights)
    
    new_weights_1 = weight_adjuster.apply_percentage_change(percentage_change_1)
    print(new_weights_1.tolist())
    
    new_weights_2 = weight_adjuster.apply_percentage_change(percentage_change_2)
    print(new_weights_2.tolist())