import secrets

def get_random_element():
    values = [1.5, 2.7, 3.1, 4.9, 5.2, 6.8, 7.3, 8.4, 9.6, 10.1]
    index = secrets.randbelow(10)
    return values[index]

if __name__ == '__main__':
    result = get_random_element()
    print(result)