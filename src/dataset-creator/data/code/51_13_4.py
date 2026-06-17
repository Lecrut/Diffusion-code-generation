class OptimizedList:
    def __init__(self):
        self.head = None
    def add(self, value):
        new_node = {'value': value, 'next': None}
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current['next']:
                current = current['next']
            current['next'] = new_node
    def get_head(self):
        return self.head
if __name__ == '__main__':
    list_instance = OptimizedList()
    sample_values = [10, 20, 30]
    for val in sample_values:
        list_instance.add(val)
    head_node = list_instance.get_head()
    print(head_node['value'])