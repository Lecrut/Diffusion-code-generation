class MyObject:
    def __init__(self, value):
        self.value = value
    def attribute(self):
        return self.value
def calculate_total_attribute_sum(collection):
    total_sum = 0
    for obj in collection:
        total_sum += obj.attribute()
    return total_sum
if __name__ == '__main__':
    data = [MyObject(10), MyObject(25), MyObject(7)]
    result = calculate_total_attribute_sum(data)
    print(result)