class ThresholdFilter:
    def __init__(self):
        self.data = {}
    
    def add_item(self, key, value):
        if key not in self.data or value > self.data[key]:
            self.data[key] = value
    
    def filter_by_threshold(self, threshold):
        return {key: value for key, value in self.data.items() if value > threshold}

if __name__ == '__main__':
    filter_instance = ThresholdFilter()
    filter_instance.add_item("apple", 3.50)
    filter_instance.add_item("banana", 2.75)
    filter_instance.add_item("cherry", 1.00)
    filter_instance.add_item("date", 4.00)
    
    filtered_prices = filter_instance.filter_by_threshold(2.00)
    print(filtered_prices)