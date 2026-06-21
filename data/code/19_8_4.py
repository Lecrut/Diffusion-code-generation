import random

def get_random_value(int_list, start, stop):
    index = random.randint(start, stop - 1)
    return int_list[index]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    r = range(3)
    result = get_random_value(data, r.start, r.stop)
    print(result)