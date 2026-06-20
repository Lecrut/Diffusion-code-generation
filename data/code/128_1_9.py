def check_negative_numbers():
    numbers = [-5, 0, 3, -2]
    negative_numbers = [num for num in numbers if num < 0]
    return negative_numbers

if __name__ == '__main__':
    print(check_negative_numbers())