class ListCounter:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_count(self):
        count = 0
        for item in self.items:
            count += 1
        return count

if __name__ == '__main__':
    counter = ListCounter()
    sample_list = [1, 2, 3, 4, 5]
    for item in sample_list:
        counter.add_item(item)
    print(counter.get_count())