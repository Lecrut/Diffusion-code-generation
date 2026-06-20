def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [5, -10, 0, 3, -7]
    for num in sample_values:
        print(f"{num} is odd: {is_odd(num)}")