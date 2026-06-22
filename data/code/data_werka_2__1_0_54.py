class WeightManager:
    def __init__(self):
        self.weights = {}

    def store_weight(self, key, weight):
        if not isinstance(key, str) or not isinstance(weight, (int, float)):
            raise ValueError('Invalid input types')
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f'Key {key} not found')
        if not isinstance(new_weight, (int, float)):
            raise ValueError('Invalid weight type')
        self.weights[key] = new_weight

if __name__ == '__main__':
    wm = WeightManager()
    sample_key = 'Bob'
    sample_weight = 75.3
    wm.store_weight(sample_key, sample_weight)
    print(f'Retrieved weight for {sample_key}:', wm.retrieve_weight(sample_key))
    updated_weight = 80.2
    wm.update_weight(sample_key, updated_weight)
    print(f'Updated weight for {sample_key}:', wm.retrieve_weight(sample_key))