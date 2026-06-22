import random
def pick_random(iterable):
    return random.choice(iterable)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = pick_random(sample_data)
    print(result)