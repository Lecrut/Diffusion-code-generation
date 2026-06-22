class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def add_number(self, number):
        if isinstance(number, (int, float)):
            self.data.append(number)

    def find_largest_number(self):
        if not self.data:
            return None
        return max(self.data)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_number(10)
    processor.add_number(5)
    processor.add_number(20)
    processor.add_number(8)
    processor.add_number(15)
    
    print(f"Largest number: {processor.find_largest_number()}")

    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_number(-5)
    processor.add_number(-1)
    processor.add_number(-10)
    processor.add_number(-3)
    
    print(f"Largest number: {processor.find_largest_number()}")

    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_number(42)
    
    print(f"Largest number: {processor.find_largest_number()}")