MAX_TERMS = 10

def generate_sequence(n):
    return n**2 + n

def main():
    for i in range(1, MAX_TERMS + 1):
        print(generate_sequence(i))

if __name__ == '__main__':
    main()