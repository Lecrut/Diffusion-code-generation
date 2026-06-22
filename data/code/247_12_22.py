ADDEND_1 = 5
ADDEND_2 = 3

def add_two_numbers(a=ADDEND_1, b=ADDEND_2):
    return a + b

if __name__ == '__main__':
    result = add_two_numbers()
    print(result)