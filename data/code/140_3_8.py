is_safe_temp = lambda temp: 15 <= temp <= 30
if __name__ == '__main__':
    print(is_safe_temp(20))
    print(is_safe_temp(14))
    print(is_safe_temp(31))