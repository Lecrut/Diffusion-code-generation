class DataHandler:
    def __init__(self, data):
        self.data = data

    def compute_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    handler1 = DataHandler([10, 20, 30, 40])
    print(handler1.compute_mean())

    handler2 = DataHandler([5, 15, 25])
    print(handler2.compute_mean())

    handler3 = DataHandler([-10, -20, -30, -40])
    print(handler3.compute_mean())