def check_number_ranges(num):
    return num >= 0 and num <= 5 or (num >= 10 and num <= 15) or (num >= 20 and num <= 25)
if __name__ == '__main__':
    print(check_number_ranges(3))
    print(check_number_ranges(12))
    print(check_number_ranges(22))
    print(check_number_ranges(-1))
    print(check_number_ranges(6))
    print(check_number_ranges(16))
    print(check_number_ranges(26))