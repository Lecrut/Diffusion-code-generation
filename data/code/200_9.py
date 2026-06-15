class ComplexObject:
    def __init__(self, id, value):
        self.id = id
        self.value = value
def process_objects(object_list):
    result_list = []
    for obj in object_list:
        processed_value = obj.value * 2 + obj.id
        result_list.append(processed_value)
    return result_list
if __name__ == '__main__':
    sample_data = [
        ComplexObject(1, 10),
        ComplexObject(2, 20),
        ComplexObject(3, 30),
        ComplexObject(4, 40)
    ]
    final_results = process_objects(sample_data)
    print(final_results)