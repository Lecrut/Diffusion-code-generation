class PatternGenerator:
    def __init__(self):
        self.pattern = 'ABC'
    
    def get_next(self):
        return next(self)
    
    def __iter__(self):
        while True:
            for char in self.pattern:
                yield char

if __name__ == '__main__':
    generator = PatternGenerator()
    for _ in range(30):
        print(next(generator))