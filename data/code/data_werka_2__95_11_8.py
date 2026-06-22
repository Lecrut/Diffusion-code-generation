class TripletValidator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate(self):
        values = (self.a, self.b, self.c)
        for val in values:
            if val <= 0:
                return False
            if val % 2 != 0:
                return False
            if val >= 100:
                return False
        return True

if __name__ == '__main__':
    v1 = TripletValidator(10, 20, 30)
    print(v1.validate())
    v2 = TripletValidator(10, 21, 30)
    print(v2.validate())
    v3 = TripletValidator(-10, 20, 30)
    print(v3.validate())
    v4 = TripletValidator(10, 20, 100)
    print(v4.validate())