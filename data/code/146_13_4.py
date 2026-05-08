class DecisionMaker:
    def process_data(self, value1, value2):
        if value1 > 10 and value2 < 5:
            return "Condition A met"
        elif value1 <= 10 and value2 >= 5:
            return "Condition B met"
        elif value1 > 5 and value2 > 10:
            return "Condition C met"
        else:
            return "Default condition"
if __name__ == '__main__':
    dm = DecisionMaker()
    data1 = 15
    data2 = 3
    result1 = dm.process_data(data1, data2)
    print(f"Data: ({data1}, {data2}), Result: {result1}")
    data3 = 10
    data4 = 7
    result2 = dm.process_data(data3, data4)
    print(f"Data: ({data3}, {data4}), Result: {result2}")
    data5 = 6
    data6 = 12
    result3 = dm.process_data(data5, data6)
    print(f"Data: ({data5}, {data6}), Result: {result3}")
    data7 = 2
    data8 = 1
    result4 = dm.process_data(data7, data8)
    print(f"Data: ({data7}, {data8}), Result: {result4}")