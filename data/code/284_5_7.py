import random

class NumberReverser:
    def __init__(self):
        self.random_numbers = []
    
    def generate_numbers(self, count):
        for _ in range(count):
            self.random_numbers.append(random.randint(1, 100))
    
    def reverse_list(self):
        start = 0
        end = len(self.random_numbers) - 1
        while start < end:
            self.random_numbers[start], self.random_numbers[end] = self.random_numbers[end], self.random_numbers[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    reverser = NumberReverser()
    reverser.generate_numbers(10)
    print("Original list:", reverser.random_numbers)
    reverser.reverse_list()
    print("Reversed list:", reverser.random_numbers)