import secrets

def get_random_element():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]
    index = secrets.randbelow(10)
    return numbers[index]

if __name__ == '__main__':
    print(get_random_element())