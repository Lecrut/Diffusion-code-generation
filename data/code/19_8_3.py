import random

def get_random_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    index = random.randrange(len(numbers))
    return numbers[index]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = get_random_value(data)
    print(result)