THRESHOLD_A = 10
THRESHOLD_B = 5
THRESHOLD_C = 20

def evaluate_conditions(value1, value2, value3):
    if value1 > THRESHOLD_A and value2 < THRESHOLD_B:
        return 'Condition A met'
    elif value1 <= THRESHOLD_A and value2 >= THRESHOLD_B:
        if value3 > THRESHOLD_C:
            return 'Condition B met (High)'
        else:
            return 'Condition B met (Low)'
    elif value1 > THRESHOLD_B and value2 > 15:
        return 'Condition C met'
    else:
        return 'Default Condition'
if __name__ == '__main__':
    data1 = 12
    data2 = 3
    data3 = 15
    print(evaluate_conditions(data1, data2, data3))