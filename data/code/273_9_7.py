class Repeater:
    def __init__(self, n):
        self.n = n

    def repeat(self, func):
        return lambda *args, **kwargs: [func(*args, **kwargs) for _ in range(self.n)]

if __name__ == '__main__':
    repeater = Repeater(5)
    greet = repeater.repeat(lambda name: print(f"Hello, {name}"))
    greet("Alice")