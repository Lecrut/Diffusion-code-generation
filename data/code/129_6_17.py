from operator import itemgetter

class CustomObject:
    def __init__(self, timestamp, priority):
        self.timestamp = timestamp
        self.priority = priority

def validate_objects(objects):
    for obj in objects:
        if not isinstance(obj, CustomObject) or not hasattr(obj, 'timestamp') or not hasattr(obj, 'priority'):
            raise ValueError("All elements must be instances of CustomObject with 'timestamp' and 'priority' attributes")

def sort_custom_objects(objects):
    validate_objects(objects)
    return sorted(objects, key=itemgetter('timestamp'), reverse=False) + \
           sorted(objects, key=itemgetter('priority'), reverse=True)

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