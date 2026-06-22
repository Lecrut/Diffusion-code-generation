import secrets

def get_random_float():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
    index = secrets.randbelow(len(numbers))
    return numbers[index]

if __name__ == '__main__':
    result = get_random_float()
    print(result)