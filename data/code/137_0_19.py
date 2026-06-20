EVEN_MASK = 1

def check_even_odd(number):
    return (number & EVEN_MASK) == 0

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 6]
    for value in sample_values:
        result = check_even_odd(value)
        print(f"Input: {value}, Is Even: {result}")