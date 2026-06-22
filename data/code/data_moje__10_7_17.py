class IntegerProducer:
    def __init__(self):
        self.values = (100, 200, 300)
        self.index = 0

    def get_next(self):
        if self.index < len(self.values):
            val = self.values[self.index]
            self.index += 1
            return val
        raise StopIteration

    def get_all(self):
        result = []
        temp_index = self.index
        for i in range(temp_index, len(self.values)):
            result.append(self.values[i])
        return result

if __name__ == '__main__':
    producer = IntegerProducer()
    first_value = producer.get_next()
    print(first_value)
    remaining = producer.get_all()
    print(remaining)