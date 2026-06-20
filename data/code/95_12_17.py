def check_input(value):
    return value > 0 and value % 2 == 0 and value < 100

if __name__ == '__main__':
    sample_values = (4, 6, 8)
    if all(check_input(val) for val in sample_values):
        print("All inputs are positive even numbers less than 100.")
    else:
        print("Not all inputs meet the criteria.")