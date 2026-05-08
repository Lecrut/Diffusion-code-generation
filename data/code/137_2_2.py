class DecisionMaker:
    def categorize_number(self, number):
        if number > 0:
            return "positive"
        elif number < 0:
            return "negative"
        else:
            return "zero"
if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.categorize_number(10))
    print(dm.categorize_number(-5))
    print(dm.categorize_number(0))
    print(dm.categorize_number(12345))
    print(dm.categorize_number(-99))