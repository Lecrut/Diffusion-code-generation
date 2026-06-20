def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_numbers = [-5, 0, 15]
    for num in sample_numbers:
        result = is_negative(num)
        print(f"Testing number: {num}, Is negative: {result}")