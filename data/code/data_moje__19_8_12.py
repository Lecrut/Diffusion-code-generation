import random

def select_random_value():
    numbers = [10, 20, 30, 40, 50]
    indices = range(len(numbers))
    random_index = random.choice(list(indices))
    return numbers[random_index]

if __name__ == '__main__':
    print(select_random_value())