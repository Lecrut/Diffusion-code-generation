import numpy as np

class WeightAdjuster:
    def __init__(self, weights):
        if not isinstance(weights, (list, np.ndarray)):
            raise ValueError('Weights must be a list or numpy array.')
        if not all(isinstance(w, (int, float)) for w in weights):
            raise ValueError('All elements in weights must be numbers.')
        self.weights = np.array(weights)

    def adjust(self, percentage_change):
        if not isinstance(percentage_change, (int, float)):
            raise ValueError('Percentage change must be a number.')
        return (self.weights * (1 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 75.3, 80.4]
    adjuster = WeightAdjuster(sample_weights)
    percentage_change_1 = 0.05
    new_weights_1 = adjuster.adjust(percentage_change_1)
    print(new_weights_1)

    percentage_change_2 = -0.02
    new_weights_2 = adjuster.adjust(percentage_change_2)
    print(new_weights_2)