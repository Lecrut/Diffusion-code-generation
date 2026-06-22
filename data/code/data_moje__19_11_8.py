import secrets

def get_random_element():
    numbers = [1.5, 2.3, 3.7, 4.9, 5.1, 6.6, 7.2, 8.8, 9.4, 10.0]
    index = secrets.randbelow(10)
    return numbers[index]

if __name__ == '__main__':
    print(get_random_element())