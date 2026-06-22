def print_positive_numbers():
    for i in range(-10, 11):
        if i > 0:
            print(i)

if __name__ == '__main__':
    print("Positive numbers from -10 to 10:")
    print_positive_numbers()