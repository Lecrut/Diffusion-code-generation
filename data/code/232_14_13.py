SQUARED_INDEX_CONST = 2

def print_squared_sequence(iterations):
    for i in range(1, iterations + 1):
        print(i ** SQUARED_INDEX_CONST)

if __name__ == '__main__':
    print_squared_sequence(5)