def is_positive_even_and_below_100(number):
    return number > 0 and number % 2 == 0 and number < 100

if __name__ == '__main__':
    sample_values = [34, -5, 78, 102, 6]
    for value in sample_values:
        if is_positive_even_and_below_100(value):
            print(f"{value} is positive, even, and less than 100.")
        else:
            print(f"{value} does not meet the conditions.")