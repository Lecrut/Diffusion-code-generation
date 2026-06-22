MAX_NUMBER = 99

def print_even_numbers():
    for num in range(MAX_NUMBER + 1):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    print_even_numbers()