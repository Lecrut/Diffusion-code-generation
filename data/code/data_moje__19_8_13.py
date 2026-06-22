import random

def select_random_value(numbers):
    index = random.randrange(len(numbers))
    return numbers[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = select_random_value(sample_list)
    print(result)