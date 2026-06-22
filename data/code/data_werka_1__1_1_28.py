class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, user_id, weight):
        self.weights[user_id] = weight

    def retrieve_weight(self, user_id):
        return self.weights.get(user_id, None)

    def update_weight(self, user_id, new_weight):
        if user_id in self.weights:
            self.weights[user_id] = new_weight
            return True
        return False
if __name__ == '__main__':
    weight_manager = WeightManager()
    weight_manager.store_weight('user1', 70.5)
    weight_manager.store_weight('user2', 68.2)
    print(weight_manager.retrieve_weight('user1'))
    print(weight_manager.update_weight('user2', 69.0))
    print(weight_manager.retrieve_weight('user2'))