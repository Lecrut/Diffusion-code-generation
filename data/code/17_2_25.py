def is_even(num):
    return num % 2 == 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    for value in sample_values:
        print(f"{value} is even: {is_even(value)}")