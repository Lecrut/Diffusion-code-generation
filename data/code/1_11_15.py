class WeightManager:
    def __init__(self):
        self._weights = {}

    def store_weight(self, identifier, weight):
        if not isinstance(identifier, str) or not identifier:
            raise ValueError("Identifier must be a non-empty string")
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self._weights[identifier] = float(weight)

    def get_weight(self, identifier):
        if identifier not in self._weights:
            raise KeyError(f"No weight found for identifier: {identifier}")
        return self._weights[identifier]

    def update_weight(self, identifier, new_weight):
        if identifier not in self._weights:
            raise KeyError(f"Identifier not found: {identifier}")
        if not isinstance(new_weight, (int, float)):
            raise ValueError("New weight must be a number")
        self._weights[identifier] = float(new_weight)

    def delete_weight(self, identifier):
        if identifier not in self._weights:
            raise KeyError(f"Identifier not found: {identifier}")
        del self._weights[identifier]

    def list_weights(self):
        return dict(self._weights)

    def has_weight(self, identifier):
        return identifier in self._weights

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("user1", 70.5)
    manager.store_weight("user2", 85.2)
    manager.store_weight("user3", 62.8)
    
    retrieved_weight = manager.get_weight("user1")
    print(f"Retrieved weight for user1: {retrieved_weight}")
    
    manager.update_weight("user1", 71.0)
    updated_weight = manager.get_weight("user1")
    print(f"Updated weight for user1: {updated_weight}")
    
    all_weights = manager.list_weights()
    print(f"All weights: {all_weights}")
    
    has_user1 = manager.has_weight("user1")
    print(f"Has user1: {has_user1}")
    
    has_user4 = manager.has_weight("user4")
    print(f"Has user4: {has_user4}")
    
    manager.delete_weight("user2")
    weights_after_delete = manager.list_weights()
    print(f"Weights after deleting user2: {weights_after_delete}")