import sys

class DataAccessor:
    def __init__(self, data):
        self.data = data
    
    def get_third(self):
        try:
            return self.data[2]
        except IndexError:
            return None

def main():
    sample_values = [5, 12, 88, 33, 9]
    accessor = DataAccessor(sample_values)
    print(accessor.get_third())

if __name__ == '__main__':
    main()