import random
def pick_random(iterable):
    return random.choice(iterable)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = pick_random(sample_list)
    print(result)