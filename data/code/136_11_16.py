def check_number_ranges(number):
    return number >= 10 and number <= 20 or (number >= 30 and number <= 40)
if __name__ == '__main__':
    print(check_number_ranges(15))
    print(check_number_ranges(25))
    print(check_number_ranges(35))
    print(check_number_ranges(45))