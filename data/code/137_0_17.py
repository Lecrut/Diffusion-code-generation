def check_even_odd(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [4, 7, 18, 23]
    for value in sample_values:
        print(f"Input: {value}, Is Even: {check_even_odd(value)}")