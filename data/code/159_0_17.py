def is_odd(number):
    return number % 2 != 0

def filter_out_odds(numbers):
    odd_numbers = list(filter(is_odd, numbers))
    return odd_numbers

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_out_odds(input_list)
    print(result)