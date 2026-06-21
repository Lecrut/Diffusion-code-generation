def is_odd(number):
    return number % 2 != 0

def find_odd_numbers(start, end):
    odd_numbers = [num for num in range(start, end + 1) if is_odd(num)]
    return odd_numbers

if __name__ == '__main__':
    sample_start = 1
    sample_end = 50
    result = find_odd_numbers(sample_start, sample_end)
    print(result)