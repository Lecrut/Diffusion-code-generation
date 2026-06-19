def first_element_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    return wrapper

@first_element_decorator
def retrieve_items():
    return [10, 20, 30, 40]

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @first_element_decorator
    def process_data(self):
        return self.data

if __name__ == '__main__':
    print(retrieve_items())
    
    processor = DataProcessor([100, 200, 300, 400])
    print(processor.process_data())