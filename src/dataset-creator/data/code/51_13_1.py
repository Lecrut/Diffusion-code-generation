class OptimizedList:
    def __init__(self):
        self._head = None
    def add(self, value):
        new_node = {'value': value, 'next': None}
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current['next']:
                current = current['next']
            current['next'] = new_node
    def get_head(self):
        return self._head
if __name__ == '__main__':
    sample_list = OptimizedList()
    sample_list.add(10)
    sample_list.add(20)
    sample_list.add(30)
    head_data = sample_list.get_head()
    print(head_data['value'])