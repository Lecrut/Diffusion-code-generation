class WeightManager:
    def __init__(self):
        self._weights = {}

    def add_weight(self, identifier, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self._weights[identifier] = weight

    def get_weight(self, identifier):
        if identifier not in self._weights:
            raise KeyError(f"Identifier {identifier} not found")
        return self._weights[identifier]

    def update_weight(self, identifier, weight):
        if identifier not in self._weights:
            raise KeyError(f"Identifier {identifier} not found")
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        self._weights[identifier] = weight

    def remove_weight(self, identifier):
        if identifier not in self._weights:
            raise KeyError(f"Identifier {identifier} not found")
        del self._weights[identifier]

    def get_all_weights(self):
        return dict(self._weights)

if __name__ == '__main__':
    manager = WeightManager()
    manager.add_weight("person_a", 70.5)
    manager.add_weight("person_b", 85.0)
    
    weight_a = manager.get_weight("person_a")
    print(weight_a)
    
    manager.update_weight("person_a", 71.0)
    current_weight = manager.get_weight("person_a")
    print(current_weight)
    
    all_weights = manager.get_all_weights()
    print(all_weights)