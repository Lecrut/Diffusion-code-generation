class StringFilter:
    def __init__(self, data):
        self.data = data

    def remove_target(self, target):
        return [item for item in self.data if item != target]

if __name__ == '__main__':
    filter_instance = StringFilter(["apple", "banana", "cherry", "date"])
    filtered_list = filter_instance.remove_target("banana")
    print(filtered_list)