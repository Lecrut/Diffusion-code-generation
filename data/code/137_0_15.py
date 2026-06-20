EVEN_MASK = 1

def check_even_odd(number):
    return (number & EVEN_MASK) == 0

if __name__ == '__main__':
    sample_values = [2, 5, 8, 13, 16]
    for value in sample_values:
        print(f"Input: {value}, Output: {check_even_odd(value)}")