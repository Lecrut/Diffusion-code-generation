class WeightManager:

    def __init__(self):
        self.weights = {}

    def store_weight(self, person, weight):
        self.weights[person] = weight

    def retrieve_weight(self, person):
        return self.weights.get(person, None)

    def update_weight(self, person, new_weight):
        if person in self.weights:
            self.weights[person] = new_weight
            return True
        return False
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight('Alice', 65.5)
    wm.store_weight('Bob', 70.2)
    print(wm.retrieve_weight('Alice'))
    updated = wm.update_weight('Bob', 71.0)
    print(updated)
    print(wm.retrieve_weight('Bob'))
    print(wm.retrieve_weight('Charlie'))