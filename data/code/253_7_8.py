class FindTheMiddleValueAmongThreeManager:
    def __init__(self):
        self.entries = []
    
    @staticmethod
    def find_median(numbers):
        if len(numbers) != 3:
            raise ValueError("Input list must contain exactly three numbers.")
        sorted_numbers = sorted(numbers)
        median = sorted_numbers[1]
        return median
    
    def add_entry(self, value):
        self.entries.append(value)
    
    def update_entry(self, index, value):
        if 0 <= index < len(self.entries):
            self.entries[index] = value
    
    def list_entries(self):
        return self.entries

if __name__ == '__main__':
    manager = FindTheMiddleValueAmongThreeManager()
    manager.add_entry(5)
    manager.add_entry(2)
    manager.add_entry(8)
    print("Initial entries:", manager.list_entries())
    median_value = FindTheMiddleValueAmongThreeManager.find_median(manager.entries)
    print("Median value:", median_value)