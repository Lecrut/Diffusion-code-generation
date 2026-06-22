MAX_NUMBER = 100

def generate_growing_numbers(N):
    return range(1, min(N + 1, MAX_NUMBER + 1))

if __name__ == '__main__':
    print(list(generate_growing_numbers(5)))