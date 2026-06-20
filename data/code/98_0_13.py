def evaluate_conditions(x, y, z):
    if x > 10 and y < 3:
        outcome = "Condition A met"
    elif z == 0:
        outcome = "Condition B met"
    else:
        outcome = "No specific condition met"
    return outcome

if __name__ == '__main__':
    sample_x = 12
    sample_y = 1
    sample_z = 5
    result = evaluate_conditions(sample_x, sample_y, sample_z)
    print(result)

    sample_x = 8
    sample_y = 4
    sample_z = 0
    result = evaluate_conditions(sample_x, sample_y, sample_z)
    print(result)