import secrets

def get_random_element(values):
    index = secrets.randbelow(len(values))
    return values[index]

if __name__ == '__main__':
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1]
    result = get_random_element(numbers)
    print(result)