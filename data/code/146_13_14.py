def evaluate_conditions(value1, value2, value3):
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
    data1 = 12
    data2 = 3
    data3 = 15
    result = evaluate_conditions(data1, data2, data3)
    print(result)