MAX_VALUE = 100

def are_valid(num):
    return num > 0 and num % 2 == 0 and num < MAX_VALUE

if __name__ == '__main__':
    print(are_valid(42))
    print(are_valid(99))
    print(are_valid(100))
    print(are_valid(-5))
    print(are_valid(3))