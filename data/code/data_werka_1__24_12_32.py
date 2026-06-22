def check_negativity(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, 0]
    for value in sample_values:
        print(f"{value}: {check_negativity(value)}")