def evaluate_conditions(value1, value2, value3):
    if value1 > 10 and value2 < 5:
        return "Condition A met"
    if value1 <= 10 and value2 >= 5 and value3 > 20:
        return "Condition B met (High)"
    if value1 <= 10 and value2 >= 5 and value3 <= 20:
        return "Condition B met (Low)"
    if value1 > 5 and value2 > 15:
        return "Condition C met"
    return "Default Condition"

if __name__ == '__main__':
    data1 = 12
    data2 = 3
    data3 = 15
    print(evaluate_conditions(data1, data2, data3))