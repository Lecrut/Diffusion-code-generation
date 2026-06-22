def print_numbers():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    try:
        print_numbers()
    except Exception as e:
        print(f"An error occurred: {e}")