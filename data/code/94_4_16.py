def check_existence(data_list):
    return bool(data_list) and any(data_list)

if __name__ == '__main__':
    print(check_existence([False, False]))
    print(check_existence([True, False]))
    print(check_existence([]))