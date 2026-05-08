import sys
def check_zero_sample(number):
    if number == 0:
        return "The number is zero."
    else:
        return "The number is not zero."
if __name__ == '__main__':
    sample_values = [0, 5, -3, 0.0]
    for value in sample_values:
        result = check_zero_sample(value)
        print(result)