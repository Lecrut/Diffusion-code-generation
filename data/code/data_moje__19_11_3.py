import secrets

numbers = [3.14, 2.71, 1.41, 0.57, 9.81, 6.02, 1.62, 7.39, 4.23, 8.16]

def get_random_element():
    index = secrets.randbelow(len(numbers))
    return numbers[index]

if __name__ == '__main__':
    result = get_random_element()
    print(result)