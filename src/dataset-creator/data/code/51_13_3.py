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
        return {'value': self.head.get('value', None), 'exists': bool(self.head)}
if __name__ == '__main__':
    ol = OptimizedList()
    ol.add(10)
    ol.add(20)
    ol.add(30)
    result = ol.get_head()
    print(result['value'])