def get_seven_times_table():
    return [str(7 * i) for i in range(1, 11)]

if __name__ == '__main__':
    result = get_seven_times_table()
    print(result)