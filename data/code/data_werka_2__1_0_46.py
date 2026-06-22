class WeightManager:
    def __init__(self):
        self.weights = {}

    def _validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError('Key must be a string')

    def _validate_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError('Weight must be a number')

    def store_weight(self, key, weight):
        self._validate_key(key)
        self._validate_weight(weight)
        self.weights[key] = weight

    def retrieve_weight(self, key):
        self._validate_key(key)
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        self._validate_key(key)
        if key not in self.weights:
            raise KeyError(f'Key {key} not found')
        self._validate_weight(new_weight)
        self.weights[key] = new_weight

if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    print(wm.retrieve_weight('Alice'))
    try:
        wm.update_weight('Bob', 70.3)
    except KeyError as e:
        print(e)