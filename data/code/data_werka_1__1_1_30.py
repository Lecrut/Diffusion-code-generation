class WeightManager:

    def __init__(self):
        self.weights = {}

    def add_weight(self, date, weight):
        self.weights[date] = weight

    def get_weight(self, date):
        return self.weights.get(date, None)

    def update_weight(self, date, new_weight):
        if date in self.weights:
            self.weights[date] = new_weight
            return True
        return False
if __name__ == '__main__':
    wm = WeightManager()
    wm.add_weight('2023-10-01', 70.5)
    wm.add_weight('2023-10-02', 71.0)
    print(wm.get_weight('2023-10-01'))
    print(wm.update_weight('2023-10-02', 71.5))
    print(wm.get_weight('2023-10-02'))
    print(wm.get_weight('2023-10-03'))