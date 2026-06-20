from operator import itemgetter

class CustomObject:
    def __init__(self, timestamp, priority):
        self.timestamp = timestamp
        self.priority = priority

    def __repr__(self):
        return f"CustomObject(timestamp={self.timestamp}, priority={self.priority})"

def sort_custom_objects(objects):
    primary_key = itemgetter('timestamp')
    secondary_key = itemgetter('priority')
    return sorted(objects, key=lambda obj: (primary_key(obj), -secondary_key(obj)))

if __name__ == '__main__':
    objects = [
        CustomObject(3, 2),
        CustomObject(1, 1),
        CustomObject(2, 3),
        CustomObject(1, 2)
    ]
    sorted_objects = sort_custom_objects(objects)
    print(sorted_objects)