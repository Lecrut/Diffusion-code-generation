import random

def get_random_item(t):
    if not t:
        return None
    return random.choice(t)

if __name__ == '__main__':
    data = (1, 2, 3, 4, 5)
    result = get_random_item(data)
    print(result)
    empty_data = ()
    empty_result = get_random_item(empty_data)
    print(empty_result)