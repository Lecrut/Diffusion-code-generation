class Counter:

    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0
if __name__ == '__main__':
    counter1 = Counter(0)
    counter2 = Counter(5)
    print(counter1.is_zero())
    print(counter2.is_zero())