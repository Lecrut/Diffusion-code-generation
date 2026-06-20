def check_number_ranges(num):
    return num >= 0 and num <= 50 or (num > 100 and num <= 200)
if __name__ == '__main__':
    print(check_number_ranges(30))
    print(check_number_ranges(150))
    print(check_number_ranges(-10))
    print(check_number_ranges(250))