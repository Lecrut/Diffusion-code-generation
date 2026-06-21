class WeightManager:
    _VALID_TYPES = (int, float)

    def __init__(self):
        self.weights = {}

    @staticmethod
    def _validate_key(key):
        if not isinstance(key, str):
            raise ValueError('Key must be a string.')

    @staticmethod
    def _validate_weight(weight):
        if not isinstance(weight, WeightManager._VALID_TYPES):
            raise ValueError('Weight must be an integer or float.')

    def store_weight(self, key, weight):
        self._validate_key(key)
        self._validate_weight(weight)
        self.weights[key] = weight

    def retrieve_weight(self, key):
        return self.weights.get(key, None)

    def update_weight(self, key, new_weight):
        if key not in self.weights:
            raise KeyError(f'Key {key} not found.')
        self._validate_weight(new_weight)
        self.weights[key] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 60.5)
    wm.store_weight('Bob', 72.3)
    print(wm.retrieve_weight('Alice'))
    wm.update_weight('Bob', 74.0)
    print(wm.retrieve_weight('Bob'))