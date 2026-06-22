import random

class RandomPicker:
    def __init__(self, iterable):
        self.data = list(iterable)
    
    def pick_one(self):
        return random.choice(self.data)
    
    def pick_multiple(self, count):
        return [random.choice(self.data) for _ in range(count)]

if __name__ == '__main__':
    items = [7, 14, 21, 28, 35]
    picker = RandomPicker(items)
    print(picker.pick_one())
    print(picker.pick_multiple(3))