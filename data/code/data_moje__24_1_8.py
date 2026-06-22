YEAR_DIVISOR = 4
HUNDRED = 100
FOUR_HUNDRED = 400

def check_leap_status(yr):
    if yr % FOUR_HUNDRED == 0:
        return True
    if yr % HUNDRED == 0:
        return False
    if yr % YEAR_DIVISOR == 0:
        return True
    return False

if __name__ == '__main__':
    print(check_leap_status(2024))
    print(check_leap_status(1900))
    print(check_leap_status(2000))