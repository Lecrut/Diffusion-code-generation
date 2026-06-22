import secrets

def print_random_element():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
    index = secrets.randbelow(len(numbers))
    value = numbers[index]
    print(value)
    return value

if __name__ == '__main__':
    print_random_element()