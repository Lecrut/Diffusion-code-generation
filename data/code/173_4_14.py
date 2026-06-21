import operator

def group_by_attribute(objects, attr):
    return operator.itemgetter(attr)(objects)

if __name__ == '__main__':
    class SampleObject:
        def __init__(self, name, category):
            self.name = name
            self.category = category
    
    objects = [SampleObject('apple', 'fruit'), SampleObject('banana', 'fruit'), SampleObject('carrot', 'vegetable')]
    grouped_objects = group_by_attribute(objects, 'category')
    
    for category, items in grouped_objects.items():
        print(f"{category}: {items}")