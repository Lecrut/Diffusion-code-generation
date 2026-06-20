def is_odd(number):
    return number & 1

if __name__ == '__main__':
    sample_numbers = [7, 8, 9, 10, 11]
    odd_count = sum(is_odd(num) for num in sample_numbers)
    print(odd_count)