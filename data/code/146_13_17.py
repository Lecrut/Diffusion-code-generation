def evaluate_conditions(value1, value2, value3):
    conditions = {
        "A": (value1 > 10 and value2 < 5),
        "B": (value1 <= 10 and value2 >= 5),
        "C": (value1 > 5 and value2 > 15)
    }
    
    if conditions["A"]:
        return "Condition A met"
    elif conditions["B"] and value3 > 20:
        return "Condition B met (High)"
    elif conditions["B"] and value3 <= 20:
        return "Condition B met (Low)"
    elif conditions["C"]:
        return "Condition C met"
    else:
        return "Default Condition"

if __name__ == '__main__':
    data1 = 12
    data2 = 3
    data3 = 15
    print(evaluate_conditions(data1, data2, data3))