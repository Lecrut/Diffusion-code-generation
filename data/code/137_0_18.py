def check_even_odd(number):
    return number & 1 == 0

if __name__ == '__main__':
    sample_numbers = [4, 7, 123, 0, -2, 1]
    for num in sample_numbers:
        result = check_even_odd(num)
        print(f"Input: {num}, Is Even: {result}")