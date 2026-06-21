import secrets

def get_element_at_random_index(numbers):
    index = secrets.randbelow(len(numbers))
    return numbers[index]

def main():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]
    result = get_element_at_random_index(numbers)
    print(result)

if __name__ == '__main__':
    main()