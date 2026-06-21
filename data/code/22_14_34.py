ODD_THRESHOLD = 1

def is_odd(number):
    return number % 2 != ODD_THRESHOLD

if __name__ == '__main__':
    sample_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")