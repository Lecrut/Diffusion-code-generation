import random
def pick_random_item(iterable):
    return random.choice(iterable)
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    print(pick_random_item(sample_list))