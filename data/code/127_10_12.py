def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    sample_numbers = [3, 4, 5, -2, 0]
    for num in sample_numbers:
        print(f"Number: {num}, Is Odd: {is_odd(num)}")