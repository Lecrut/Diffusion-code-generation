class DecisionMaker:
    def process_data(self, value1, value2, value3):
        if value1 > 10 and value2 < 5:
            return "Condition A met"
        elif value1 <= 10 and value2 >= 5:
            if value3 > 20:
                return "Condition B met (High)"
            else:
                return "Condition B met (Low)"
        elif value1 > 5 and value2 > 15:
            return "Condition C met"
        else:
            return "Default Condition"
if __name__ == '__main__':
    dm = DecisionMaker()
    data1 = 12
    data2 = 3
    data3 = 15
    result1 = dm.process_data(data1, data2, data3)
    print(f"Input: ({data1}, {data2}, {data3}) -> Result: {result1}")
    data1 = 8
    data2 = 6
    data3 = 25
    result2 = dm.process_data(data1, data2, data3)
    print(f"Input: ({data1}, {data2}, {data3}) -> Result: {result2}")
    data1 = 7
    data2 = 20
    data3 = 10
    result3 = dm.process_data(data1, data2, data3)
    print(f"Input: ({data1}, {data2}, {data3}) -> Result: {result3}")
    data1 = 6
    data2 = 18
    data3 = 5
    result4 = dm.process_data(data1, data2, data3)
    print(f"Input: ({data1}, {data2}, {data3}) -> Result: {result4}")