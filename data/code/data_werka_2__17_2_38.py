EVEN_THRESHOLD = 2

def is_even(num):
    return num % EVEN_THRESHOLD == 0

if __name__ == '__main__':
    sample_values = [4, 7, 10, 13]
    for value in sample_values:
        print(f"{value} is even: {is_even(value)}")