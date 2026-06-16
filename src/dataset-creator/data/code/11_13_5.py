import json
class DeepValueComparator:
    def equals(self, a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, list):
            if len(a) != len(b):
                return False
            for x, y in zip(a, b):
                if not self.equals(x, y):
                    return False
            return True
        elif isinstance(a, dict):
            if set(a.keys()) != set(b.keys()):
                return False
            for k in a:
                if not self.equals(a[k], b[k]):
                    return False
            return True
        else:
            return a == b
if __name__ == '__main__':
    obj1 = [1, {'a': 2}, 'hello']
    obj2 = [1, {'a': 2}, 'world']
    comparator = DeepValueComparator()
    result = comparator.equals(obj1, obj2)
    print(result)