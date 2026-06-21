import secrets

class FloatSelector:
    def __init__(self):
        self.values = [1.23, 4.56, 7.89, 10.11, 13.14, 16.17, 19.20, 22.23, 25.26, 28.29]

    def get_secure_random(self):
        if len(self.values) == 0:
            raise ValueError("No values available to select from")
        index = secrets.randbelow(len(self.values))
        return self.values[index]

if __name__ == '__main__':
    selector = FloatSelector()
    print(selector.get_secure_random())