class SimpleObject:
    def __init__(self, value):
        self._value = value
    def attribute(self):
        return self._value
def calculate_total_attribute_sum(collection):
    total_sum = 0
    for obj in collection:
        total_sum += obj.attribute()
    return total_sum
if __name__ == '__main__':
    data = [SimpleObject(10), SimpleObject(25), SimpleObject(7)]
    result = calculate_total_attribute_sum(data)
    print(result)