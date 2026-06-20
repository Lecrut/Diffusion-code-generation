ADD_ONE = 1

def add_numbers(a, b):
    return int(a) + int(b) + ADD_ONE

if __name__ == '__main__':
    print(add_numbers(5, 10))
    print(add_numbers("5", "10"))
    print(add_numbers(3.5, 7))
    print(add_numbers("hello", 10))
    print(add_numbers(100, "200"))