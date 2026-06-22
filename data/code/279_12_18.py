EVEN_THRESHOLD = 2

def print_even_numbers():
    for num in range(100):
        if num % EVEN_THRESHOLD == 0:
            print(num)

if __name__ == '__main__':
    print_even_numbers()