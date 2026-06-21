from collections import deque

class IntDeque:
    def __init__(self):
        self._data = deque()

    def add(self, value):
        self._data.append(value)

    def pop_last(self):
        return self._data.pop()

def main():
    d = IntDeque()
    d.add(10)
    d.add(20)
    d.add(30)
    d.add(40)
    d.add(50)
    result = d.pop_last()
    print(result)

if __name__ == '__main__':
    main()