import random
def pick_random_item(iterable):
    return random.choice(iterable)
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    result = pick_random_item(sample_data)
    print(result)