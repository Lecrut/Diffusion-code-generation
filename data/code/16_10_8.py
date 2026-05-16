import sys
def check_positive(number):
    if number > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_inputs = [10, -5, 0, 3.14, "hello"]
    for value in sample_inputs:
        try:
            num = int(value)
            result = check_positive(num)
            print(f"Input: {value}, Is Positive: {result}")
        except ValueError:
            print(f"Input: {value}, Error: Invalid integer input.")
        except TypeError:
            print(f"Input: {value}, Error: Type error during conversion.")