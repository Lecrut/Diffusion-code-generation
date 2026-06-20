from operator import itemgetter

class CustomObject:
    def __init__(self, timestamp, priority):
        self.timestamp = timestamp
        self.priority = priority

def sort_custom_objects(objects):
    return sorted(objects, key=lambda x: (x.timestamp, -x.priority))

if __name__ == '__main__':
    objects = [
        CustomObject(3, 2),
        CustomObject(1, 1),
        CustomObject(2, 3),
        CustomObject(1, 2)
    ]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(f"Timestamp: {obj.timestamp}, Priority: {obj.priority}")