class Repeater:
    def __init__(self, times=5):
        self.times = times

    @staticmethod
    def repeat_n_times(func):
        def wrapper(*args, **kwargs):
            for _ in range(Repeater._get_repetition_count()):
                func(*args, **kwargs)
        return wrapper

    @classmethod
    def _get_repetition_count(cls):
        return cls.times

    def greet(self, name):
        print(f"Hello, {name}")

if __name__ == '__main__':
    repeater = Repeater()
    repeated_greet = repeater.repeat_n_times(repeater.greet)
    repeated_greet("Alice")