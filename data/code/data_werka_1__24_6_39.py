NEGATIVE_THRESHOLD = 0

def determine_negative_status(number):
    if number < NEGATIVE_THRESHOLD:
        return f"The value {number} is negative."
    else:
        return f"The value {number} is not negative."

if __name__ == '__main__':
    sample_values = [-20, 0, 30]
    for value in sample_values:
        print(determine_negative_status(value))