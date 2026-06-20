class WeightManager:
    def __init__(self):
        self._weights = {}

    def add_weight(self, label, value):
        self._weights[label] = value

    def get_weight(self, label):
        return self._weights.get(label)

    def update_weight(self, label, value):
        if label in self._weights:
            self._weights[label] = value
            return True
        return False

    def delete_weight(self, label):
        if label in self._weights:
            del self._weights[label]
            return True
        return False

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight("morning", 70.5)
    wm.add_weight("evening", 71.0)
    print(wm.get_weight("morning"))
    wm.update_weight("morning", 70.8)
    print(wm.get_weight("morning"))
    print(wm.get_all_weights())