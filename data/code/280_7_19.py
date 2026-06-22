EVEN = "even"
ODD = "odd"

def print_number_type(number):
    if number % 2 == 0:
        return EVEN
    else:
        return ODD

if __name__ == '__main__':
    for i in range(15):
        result = print_number_type(i)
        print(f"{i} is {result}")