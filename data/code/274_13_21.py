class EnhancedListPrinter:
    def __init__(self, items):
        self.items = items
    
    def print_items(self):
        for item in self.items:
            print(item)
    
    def count_items(self):
        return len(self.items)

if __name__ == '__main__':
    printer = EnhancedListPrinter(['apple', 'banana', 'cherry'])
    printer.print_items()
    print(f"Number of items: {printer.count_items()}")