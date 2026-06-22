import random

class RandomSelector:
    def __init__(self, data):
        self.data = data

    def get_random_element(self):
        return random.choice(self.data)

def get_random_element(lst):
    selector = RandomSelector(lst)
    return selector.get_random_element()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)