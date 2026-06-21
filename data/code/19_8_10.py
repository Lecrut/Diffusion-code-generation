import random

def select_random_value():
    values = [10, 20, 30, 40, 50]
    index = random.randrange(len(values))
    return values[index]

if __name__ == '__main__':
    result = select_random_value()
    print(result)