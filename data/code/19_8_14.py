import random

def select_random_value(values):
    index = random.randrange(len(values))
    return values[index]

if __name__ == '__main__':
    pre_defined_list = [10, 20, 30, 40, 50]
    result = select_random_value(pre_defined_list)
    print(result)