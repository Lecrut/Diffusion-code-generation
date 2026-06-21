class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, key, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError('Weight must be a number')
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f'No weight found for key: {key}')
        if not isinstance(new_weight, (int, float)):
            raise ValueError('New weight must be a number')
        self.weights[key] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    wm.store_weight('Bob', 75.3)
    print(wm.retrieve_weight('Alice'))
    wm.update_weight('Alice', 62.0)
    print(wm.retrieve_weight('Alice'))
    try:
        wm.update_weight('Charlie', 80.0)
    except KeyError as e:
        print(e)
    try:
        wm.store_weight('David', 'eighty')
    except ValueError as e:
        print(e)