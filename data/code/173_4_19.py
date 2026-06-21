import operator

def group_by_attr(objs, attr):
    return operator.itemgetter(attr)(objs)

if __name__ == '__main__':
    class SampleObject:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    objects = [SampleObject('a', 1), SampleObject('b', 2), SampleObject('c', 1)]
    grouped_by_name = group_by_attr(objects, 'name')
    grouped_by_value = group_by_attr(objects, 'value')

    print(grouped_by_name)
    print(grouped_by_value)