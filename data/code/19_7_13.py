import random
def pick_random_item(iterable):
    return random.choice(iterable)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = pick_random_item(sample_list)
    print(result)