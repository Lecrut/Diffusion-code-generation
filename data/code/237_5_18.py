def generate_sequence(n):
    return [i**2 + i for i in range(1, n+1)]

if __name__ == '__main__':
    try:
        terms = generate_sequence(10)
        print(terms)
    except Exception as e:
        print(f"An error occurred: {e}")