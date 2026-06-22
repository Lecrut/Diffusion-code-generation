THRESHOLD = 10

def evaluate_greater_than_ten(val_one, val_two):
    first_condition = val_one > THRESHOLD
    second_condition = val_two > THRESHOLD
    return first_condition or second_condition

if __name__ == '__main__':
    a = 3
    b = 15
    output = evaluate_greater_than_ten(a, b)
    print(output)