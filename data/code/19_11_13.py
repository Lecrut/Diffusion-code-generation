import secrets

class NumberSelector:
    DATA = [0.25, 1.5, 2.75, 3.0, 4.1, 5.9, 6.25, 7.5, 8.88, 9.99]

    @classmethod
    def select(cls):
        index = secrets.randbelow(len(cls.DATA))
        return cls.DATA[index]

if __name__ == '__main__':
    print(NumberSelector.select())