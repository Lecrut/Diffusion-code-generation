import random

def _validate_iterable(data):
    if not hasattr(data, '__iter__') or not hasattr(data, '__len__') or len(data) == 0:
        raise ValueError("Iterable must be non-empty and support len()")

def pick_random_item(iterable):
    _validate_iterable(iterable)
    return random.choice(iterable)

if __name__ == '__main__':
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    selected_color = pick_random_item(colors)
    print(selected_color)