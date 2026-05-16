class DecisionMaker:
    def process_data(self, value1, value2):
        if value1 > 10 and value2 < 5:
            return "Condition A met"
        elif (value1 <= 10 and value2 >= 5) or (value1 > 20):
            return "Condition B met"
        elif value1 == 10 and value2 == 5:
            return "Condition C met"
        else:
            return "Default Condition"
if __name__ == '__main__':
    dm = DecisionMaker()
    data1 = 15
    data2 = 3
    result1 = dm.process_data(data1, data2)
    print(f"Input: ({data1}, {data2}), Result: {result1}")
    data3 = 12
    data4 = 7
    result2 = dm.process_data(data3, data4)
    print(f"Input: ({data3}, {data4}), Result: {result2}")
    data5 = 10
    data6 = 5
    result3 = dm.process_data(data5, data6)
    print(f"Input: ({data5}, {data6}), Result: {result3}")
    data7 = 25
    data8 = 1
    result4 = dm.process_data(data7, data8)
    print(f"Input: ({data7}, {data8}), Result: {result4}")
    data9 = 5
    data10 = 5
    result5 = dm.process_data(data9, data10)
    print(f"Input: ({data9}, {data10}), Result: {result5}")