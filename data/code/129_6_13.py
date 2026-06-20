from operator import itemgetter

class CustomObject:
    def __init__(self, timestamp, priority):
        self.timestamp = timestamp
        self.priority = priority

def sort_custom_objects(objects):
    return sorted(objects, key=itemgetter('timestamp'), reverse=False)

if __name__ == '__main__':
    objects = [
        CustomObject(1633072800, 3),
        CustomObject(1633072800, 1),
        CustomObject(1633072801, 2),
        CustomObject(1633072801, 4)
    ]
    sorted_objects = sort_custom_objects(objects)
    for obj in sorted_objects:
        print(f"Timestamp: {obj.timestamp}, Priority: {obj.priority}")