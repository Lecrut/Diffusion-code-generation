import random

def get_random_element(data):
    return random.choice(data)

if __name__ == '__main__':
    options = ['red', 'green', 'blue', 'yellow', 'purple']
    selected = get_random_element(options)
    print(selected)