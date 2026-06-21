def evaluate_conditions(value1, value2, value3):
    condition_a = value1 > 10 and value2 < 5
    condition_b = (value1 <= 10 and value2 >= 5) and (value3 > 20 or value3 < 10)
    condition_c = value1 > 5 and value2 > 15
    if condition_a:
        return 'Condition A met'
    elif condition_b:
        return 'Condition B met'
    elif condition_c:
        return 'Condition C met'
    else:
        return 'Default Condition'
if __name__ == '__main__':
    result = evaluate_conditions(12, 3, 5)
    print(result)