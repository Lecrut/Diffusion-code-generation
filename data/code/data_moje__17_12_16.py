from collections import deque

class DequeStructure:
    def __init__(self):
        self._data = deque()

    def add(self, value):
        self._data.append(value)

    def pop_last(self):
        return self._data.pop()

def main():
    dq = DequeStructure()
    dq.add(10)
    dq.add(20)
    dq.add(30)
    dq.add(40)
    dq.add(50)

    last_item = dq.pop_last()
    print(last_item)

if __name__ == '__main__':
    main()