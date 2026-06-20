class TripletChecker:

    def __init__(self, triplets):
        self.triplets = triplets

    def is_mutually_exclusive(self):
        return sum(self.triplets) == 1
if __name__ == '__main__':
    checker1 = TripletChecker((True, False, False))
    print(checker1.is_mutually_exclusive())
    checker2 = TripletChecker((False, True, True))
    print(checker2.is_mutually_exclusive())