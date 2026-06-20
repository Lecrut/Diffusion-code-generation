from operator import itemgetter

class CustomObject:
    def __init__(self, timestamp, priority):
        self.timestamp = timestamp
        self.priority = priority

def sort_custom_objects(objects):
    return sorted(objects, key=itemgetter('timestamp'), reverse=False)

if __name__ == '__main__':
    objects = [
        CustomObject(3, 2),
        CustomObject(1, 1),
        CustomObject(2, 3)
    ]
    sorted_objects = sort_custom_objects([obj.__dict__ for obj in objects])
    print(sorted_objects)