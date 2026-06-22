class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, key, weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError('Weight must be a non-negative number')
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if not isinstance(new_weight, (int, float)) or new_weight < 0:
            raise ValueError('Weight must be a non-negative number')
        if key in self.weights:
            self.weights[key] = new_weight
        else:
            raise KeyError(f'No weight found for key: {key}')
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    wm.store_weight('Bob', 75.3)
    print(wm.retrieve_weight('Alice'))
    try:
        wm.update_weight('Alice', 62.0)
        print(wm.retrieve_weight('Alice'))
        wm.update_weight('Charlie', 80.0)
    except (ValueError, KeyError) as e:
        print(e)