def hours_to_milliseconds(hours):
    return int(hours * 3600 * 1000)

if __name__ == '__main__':
    print(hours_to_milliseconds(2))