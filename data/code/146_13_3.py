class DecisionMaker:
    def process_data(self, value1, value2):
        if value1 > 10 and value2 < 5:
            return "Condition A met"
        elif value1 <= 10 and value2 >= 5:
            return "Condition B met"
        elif value1 > 5 and value2 > 10:
            return "Condition C met"
        else:
            return "Default Condition"
if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.process_data(15, 3))
    print(dm.process_data(8, 7))
    print(dm.process_data(6, 12))
    print(dm.process_data(10, 5))
    print(dm.process_data(20, 20))