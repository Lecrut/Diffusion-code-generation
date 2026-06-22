import random
def pick_random_item(items):
    return random.choice(items)
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date']
    print(pick_random_item(sample_data))